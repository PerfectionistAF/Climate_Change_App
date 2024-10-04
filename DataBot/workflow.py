from typing import Annotated, List, Sequence
from langgraph.graph import END, StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from typing_extensions import TypedDict
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage

from llm import llm

MAX_REVISION_TIMES = 5

class State(TypedDict):
    messages: Annotated[list, add_messages]
    revision_times: int

class Writer:
    def __init__(self, llm = llm):
        workflow = StateGraph(State)
        
        workflow.add_node('writer', self.writer_call)
        workflow.add_edge(START, 'writer')
        workflow.add_node('critic', self.critic_call)
        workflow.add_edge('writer', 'critic')
        
        workflow.add_conditional_edges('critic', self.critic_condition, {True : END, False : 'writer'})
        memory = MemorySaver()
        self.graph = workflow.compile(checkpointer = memory)
    
    def writer_call(self, state):
        '''
        it should be an llm call with its system prompt
        '''

        system_prompt = f"""
        You are an excellent data analysis and a story teller, you are to write a story about the given data.
        """
        input = state['messages'][0]
    
        writer_list = [{
                'role' : 'system',
                'content' : system_prompt
            },
            {
                'role' : 'user',
                'content' : input
                }
        ]
        
        if state['revision_times'] > 0:
            writer_list.append(
                {
                    'role' : "user",
                    'content' : f"please review these notes and writer based on them {state['messages'][-1]}"
                }
            )
        output = llm.call(writer_list)
        return {'messages' :  str(output)}
        
    
    def critic_call(self, state):
        '''
        it should be an llm call with its system prompt
        '''

        system_prompt = f"""
        You are a professional story critique, given a written story, please give detailed feedback, and what to be improved.
        """
        writer_output = state['message'][-1]
        
        critic_list = [{
                'role' : 'system',
                'content' : system_prompt
            },
            {
                'role' : 'user',
                'content' : writer_output
            }
        ]
        output = self.llm.call(critic_list)

        previous_revision_times = state['revision_times']
        return {'messages' :  str(output), 'revision_times' : previous_revision_times + 1}

    def critic_condition(self, state):
        '''
        takes the last message (coming form the critic)

        if good, return True
        if bad, return False
        '''

        if state["revision_times"] >= MAX_REVISION_TIMES:
            return True 
        return False

writer = Writer()

############################################################################

import pandas as pd

file_path = "../Data/pilot_topdown_CO2_Budget_countries_v1.csv"
data = pd.read_csv(file_path)
preprocessed_data = data.to_string()
writer = Writer()
initial_state = {
    'messages': [{'role' : "user","content":preprocessed_data}],
    'revision_times': 0
}
output = writer.graph.invoke(initial_state, {'configurable' : {'thread_id' : 1, 'checkpoint_ns' : 0, 'checkpoint_id' : 0}})
print(output)