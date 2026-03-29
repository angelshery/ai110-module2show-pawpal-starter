```mermaid
classDiagram
    class Owner {
        +String name
        +int availableTime
        +List~String~ preferences
        +List~Pet~ pets
        +addPet(pet: Pet)
        +getAvailableTime() int
        +getAllTasks() List~Task~
    }

    class Pet {
        +String name
        +String species
        +int age
        +String breed
        +List~Task~ tasks
        +addTask(task: Task)
        +getTasks() List~Task~
    }

    class Task {
        +String name
        +String type
        +int duration
        +int priority
        +String startTime
        +String frequency
        +Date dueDate
        +bool completed
        +getDetails() String
        +markComplete() Task
    }

    class Scheduler {
        +List~Task~ plan
        +Owner owner
        +generatePlan(owner: Owner) List~Task~
        +sortByTime() List~Task~
        +filterTasks(petName, completed) List~Task~
        +detectConflicts() List~String~
        +explainPlan() String
    }

    Owner "1" --> "1..*" Pet : owns
    Pet "1" --> "0..*" Task : has
    Scheduler --> Owner : uses available time and tasks