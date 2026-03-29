# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler.

The Owner class stores user information such as name, available time, and preferences.

The Pet class stores pet details such as name, species, age, and breed.

The Task class represents pet care activities such as feeding, walking, medication, grooming, or enrichment. It includes important attributes like duration and priority.

The Scheduler class is responsible for generating a daily plan based on the owner's available time and the priority of tasks. It can also explain why certain tasks were selected for the plan.


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

During implementation, I made a few small changes based on feedback from Claude.

One change was simplifying the Task class. Claude initially suggested adding validation logic and strict task type checking, but I removed this to keep the design beginner-friendly and focused on the core requirements of the project.

I also improved the relationships between classes by ensuring that the Owner class properly stores pets using the add_pet() method, and that the Scheduler class keeps track of the current owner and pet when generating a plan. This will help later when explaining the scheduling decisions.

I did not apply all suggestions from the AI review, such as adding advanced validation or redesigning the system for multiple pets, because I wanted to keep the system simple and aligned with the project scope.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

My scheduler detects conflicts by checking whether two tasks share the exact same start time. For example, if Morning Walk and Medication are both scheduled at 08:00, the scheduler will flag it as a conflict.

The tradeoff is that this rule does not catch overlapping durations. For example, a 30-minute task starting at 08:00 and a 10-minute task starting at 08:15 would technically overlap, but my scheduler would not flag it because their start times are different.

This is a reasonable tradeoff for this project because the app is designed for a single owner managing a small number of daily pet tasks. Exact time conflicts are the most common and obvious problem to catch. Checking for full duration overlaps would require calculating end times and comparing time ranges, which adds complexity that is not needed at this stage.

If the app were expanded to handle many pets or precise scheduling (for example, a vet clinic), upgrading to duration-based conflict detection would be the right next step.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used Claude in VS Code throughout all four phases of the project. The most effective uses were:

- **Generating class skeletons from my UML** — asking Claude to convert my diagram into Python stubs with docstrings saved time and kept the code aligned with my design from the start.
- **Code review before implementing** — asking Claude to review my skeleton and identify missing relationships (like the Scheduler not storing the owner) helped me catch structural problems early, before any logic was written.
- **Phase-by-phase chat sessions** — I kept algorithmic planning (Phase 4 sorting, filtering, conflict detection) in a separate chat session from my core implementation. This made it much easier to stay focused because each session had a clear scope and didn't get cluttered with earlier design decisions.
- **Targeted prompts** — the most useful prompts were specific ones like "only change the generate_plan method" or "do not redesign the class structure." Vague prompts like "improve my code" produced suggestions that were too broad and harder to evaluate.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

When Claude reviewed my Task class, it suggested adding a `__post_init__` validation method with a `VALID_TASK_TYPES` list to prevent typos in task type strings. I read through the suggestion and decided to remove it. The validation added complexity that was not required by the project, and it would have made the class harder to read for a beginner audience.

I verified this decision by asking Claude directly whether the simpler version would still work for the assignment scope. It confirmed that for a small app with a fixed set of task types, keeping the class simple was the right call. This showed me that AI suggestions are not always wrong or always right — they need to be evaluated against the actual requirements and scope of what you are building.

I also noticed that Claude's conflict detection suggestion using `defaultdict` was more Pythonic than my current version, but harder to read. I kept the simpler version because readability mattered more than cleverness at this stage, and documented the tradeoff in section 2b.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I wrote pytest tests covering the following behaviors:

- **Task completion** — verifying that `mark_complete()` flips `completed` from `False` to `True`
- **Recurring tasks** — verifying that a daily task returns a new Task with `due_date + 1 day`, and that a one-off task returns `None`
- **Sorting** — verifying that tasks added out of chronological order are returned in the correct order by `sort_by_time()`, and that priority breaks ties at the same start time
- **Conflict detection** — verifying that two tasks at `"08:00"` produce exactly one warning, and that tasks at different times produce an empty list
- **Filtering** — verifying that `filter_tasks()` correctly separates tasks by pet name and by completion status
- **Edge cases** — verifying that a pet with no tasks returns an empty list without crashing, and that a scheduler with no tasks produces an empty plan

These tests were important because the scheduling logic is the core of the project. Without them, it would be easy to introduce a bug in sorting or conflict detection and not notice until the app behaved unexpectedly in the UI.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am confident the core backend logic works correctly. All tests pass, and the behaviors tested match the features shown in the Streamlit UI demo.

The areas I would test next with more time are:

- **Duration overlap conflicts** — testing that tasks at different times but overlapping durations are eventually caught once that logic is added
- **Owner with no pets** — verifying the scheduler handles this gracefully without an error
- **Recurring task integration** — testing that calling `pet.add_task(next_task)` after `mark_complete()` correctly registers the new task in the plan on the next run
- **Streamlit UI behavior** — the UI layer currently has no automated tests; testing form submissions and session state updates would increase overall confidence

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The part I am most satisfied with is the Scheduler class. It started as a simple stub and grew into a class that sorts, filters, detects conflicts, and explains its plan — all without becoming difficult to read. Each method does one thing clearly, and the logic is easy to follow even without prior experience with scheduling algorithms.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would upgrade the conflict detection from exact time matching to duration-based overlap checking. Right now, a 30-minute task at 08:00 and a 10-minute task at 08:15 would not trigger a warning, even though they overlap. Adding end time calculation would make the scheduler more realistic without requiring a full redesign.

I would also connect the recurring task logic to the Streamlit UI so users can see the next occurrence appear automatically after marking a task complete.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

The most important thing I learned is that AI works best when you already have a plan. When I came to Claude with a clear UML, specific method names, and a defined scope, the output was useful and easy to integrate. When I asked open-ended questions without constraints, the suggestions were often too complex or solved a different problem than the one I had.

Being the lead architect means deciding what to keep, what to simplify, and what to reject entirely. AI accelerated the writing of code, but every structural decision — which classes exist, how they relate, what goes in each method — came from me. That balance was the most valuable thing I took away from this project.
