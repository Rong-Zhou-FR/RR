Plan the implementation of the following project in this repository:

```
[Project name] RR (Robotika Ron)

[Project description]

Text generation AI agent to write text in Rong (author, 'me')'s style for various scenarios:

- tech guides
- code documentation
- email
- `.enc` encyclopedia entry (a custom file format based on `toml`)

[project scope]

- working AI agent with public OpenAI style API
  - reliably reproduce author's writing style
- easily modifiable system prompt+scenario-based context injection system 

[project requirements]

- principle language: python
- 100% FOSS: base-model, context system,...
- provider agnostic: for now focus on hosting on hugging face, but must be easily switchable to other providers
- modularity
  - each function does one small thing and one small thing only
  - functions that can be potentially reused must be 
  - each module fulfills one purpose
- lightweight and minimalist
  - when existing FOSS libraries fulfill already a function, import it instead of rewriting from scratch
```

## Delivrables

You must create `./dev/plans/0-init-plan.md` and in it:

- Propose at least one project architecture and illustrate it in a tree diagram
- Propose at least one tech stack and illustrate it in a markdown table
- Outline main dependencies in a multi-level markdown list for each proposed stack
- Outline a multi-phase implementation plan for your best proposal
  - with a rapid minimum viable prototype
  - and subsequent progressive improvements



## Requirements

- When there are multiple comparable alternatives, you must include both, compare them and make clear which one(s) is/are best according to your opinion and why
- You must write clearly and concisely


