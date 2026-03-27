```mermaid
classDiagram
    class Owner {
        +String name
        +int availableTime
        +List~String~ preferences
        +addPet(pet: Pet)
        +getAvailableTime() int
    }

    class Pet {
        +String name
        +String species
        +int age
        +String breed
        +addTask(task: Task)
        +getTasks() List~Task~
    }

    class Task {
        +String name
        +String type
        +int duration
        +int priority
        +getDetails() String
    }

    class Scheduler {
        +List~Task~ plan
        +generatePlan(owner: Owner, pet: Pet) List~Task~
        +explainPlan() String
    }

    Owner "1" --> "1..*" Pet : owns
    Pet "1" --> "0..*" Task : has
    Scheduler --> Owner : uses available time
    Scheduler --> Pet : reads tasks