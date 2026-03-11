#!/usr/bin/env python3
"""
Demo script showcasing basic AI Agent functionality
"""

import json
from typing import List, Dict, Any
from dataclasses import dataclass, field
from enum import Enum

class AgentRole(Enum):
    """Agent role types"""
    ASSISTANT = "assistant"
    RESEARCHER = "researcher"
    CODER = "coder"
    PLANNER = "planner"

@dataclass
class Tool:
    """Represents a tool that an agent can use"""
    name: str
    description: str
    parameters: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Message:
    """Represents a message in the conversation"""
    role: str
    content: str

class SimpleAgent:
    """A simple AI Agent implementation for demonstration"""

    def __init__(self, name: str, role: AgentRole, tools: List[Tool] = None):
        self.name = name
        self.role = role
        self.tools = tools or []
        self.memory: List[Message] = []
        self.task_history: List[str] = []

    def add_to_memory(self, role: str, content: str):
        """Add a message to agent's memory"""
        self.memory.append(Message(role=role, content=content))

    def think(self, task: str) -> str:
        """Simulate agent thinking process"""
        self.add_to_memory("user", task)
        thought = f"{self.name} is analyzing: {task}"
        self.add_to_memory("assistant", thought)
        return thought

    def use_tool(self, tool_name: str, **kwargs) -> str:
        """Simulate using a tool"""
        tool = next((t for t in self.tools if t.name == tool_name), None)
        if tool:
            result = f"{self.name} used {tool_name} with params: {kwargs}"
            self.add_to_memory("assistant", result)
            return result
        return f"Tool {tool_name} not found"

    def plan_task(self, task: str) -> List[str]:
        """Break down a task into steps"""
        steps = [
            f"1. Understand the task: {task}",
            f"2. Identify necessary tools",
            f"3. Execute the plan",
            f"4. Verify results"
        ]
        self.task_history.append(task)
        return steps

    def get_memory_summary(self) -> str:
        """Get a summary of agent's memory"""
        return f"{self.name} has {len(self.memory)} messages in memory and completed {len(self.task_history)} tasks"

def main():
    print("AI Agent Forum Demo Script")
    print("===========================\n")

    # Define available tools
    tools = [
        Tool("search", "Search for information online", {"query": "string"}),
        Tool("code", "Write or analyze code", {"language": "string", "code": "string"}),
        Tool("analyze", "Analyze data or documents", {"data": "any"})
    ]

    # Create agents
    assistant = SimpleAgent("Helper", AgentRole.ASSISTANT, tools)
    researcher = SimpleAgent("Explorer", AgentRole.RESEARCHER, tools)
    coder = SimpleAgent("DevBot", AgentRole.CODER, tools)

    agents = [assistant, researcher, coder]

    # Demonstrate agent capabilities
    print("Available Agents:")
    for agent in agents:
        print(f"  - {agent.name} ({agent.role.value})")

    print("\nAvailable Tools:")
    for tool in tools:
        print(f"  - {tool.name}: {tool.description}")

    # Agent thinking demonstration
    print("\n--- Agent Thinking Demo ---")
    task = "Research the latest AI agent frameworks"
    print(f"Task: {task}")
    thought = researcher.think(task)
    print(f"Thought: {thought}")

    # Tool usage demonstration
    print("\n--- Tool Usage Demo ---")
    result = coder.use_tool("code", language="python", code="print('Hello Agent!')")
    print(f"Result: {result}")

    # Task planning demonstration
    print("\n--- Task Planning Demo ---")
    complex_task = "Build a simple web scraper"
    print(f"Task: {complex_task}")
    steps = assistant.plan_task(complex_task)
    print("Plan:")
    for step in steps:
        print(f"  {step}")

    # Memory summary
    print("\n--- Agent Memory Summary ---")
    for agent in agents:
        print(agent.get_memory_summary())

    # Save agent state to file
    agent_data = {
        "agents": [
            {
                "name": agent.name,
                "role": agent.role.value,
                "tasks_completed": len(agent.task_history)
            }
            for agent in agents
        ]
    }

    with open('output/agent_state.json', 'w') as f:
        json.dump(agent_data, f, indent=2)

    print("\nAgent state saved to 'output/agent_state.json'")
    print("\nDemo completed successfully!")

if __name__ == "__main__":
    main()
