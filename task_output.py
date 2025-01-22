from pydantic import BaseModel, Field
from typing import List, Dict, Optional

from pydantic import BaseModel
from typing import List

# Model for each sub-task
class SubTask(BaseModel):
    sub_task_id: str
    title: str
    description: str
    actions: List[str]
    acceptance_criteria: List[str]

# Model for the main task
class Task(BaseModel):
    task_id: str
    title: str
    description: str
    sub_tasks: List[SubTask]