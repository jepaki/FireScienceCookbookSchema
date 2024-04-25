# QuestionModel

### Properties

- **`question`** *(string)*: The question to be answered.
- **`answer`** *(string)*: The answer to the question.
- **`case_studies`**: The case studies to which the question applies.
  - **All of**
    - : Refer to *[CaseStudy](#%24defs/CaseStudy)*.
- **`science_inputs`** *(array)*: The science inputs to which the question applies.
  - **Items**: Refer to *[ScienceInput](#%24defs/ScienceInput)*.
### Definitions

- <a id="%24defs/CaseStudy"></a>**`CaseStudy`** *(object)*
  - **`name`** *(string, required)*: The name of the case study.
  - **`description`** *(string, required)*: A description of the case study.
  - **`case_study`**: The name of the case study. Default: `null`.
    - **Any of**
      - *string*
      - *null*
- <a id="%24defs/ScienceInput"></a>**`ScienceInput`** *(object)*
  - **`name`** *(string, required)*: The name of the science input.
  - **`description`** *(string, required)*: A description of the science input.
  - **`science_input`**: The name of the science input. Default: `null`.
    - **Any of**
      - *string*
      - *null*

