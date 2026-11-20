def get_task_status(TaskFlow):
  return {
    "task":TaskFlow,
    "status": "completed"
  }

if __name__ == "__main__":
  task = get_task_status("Build CRUD API")
  print(task)
print("testing github project automation")
