# Question

### Properties

- **`question`** *(string)*: The question to be answered.
- **`answer`** *(array)*: The answer to the question.
  - **Items**: Refer to *[Answer](#%24defs/Answer)*.
- **`context`** *(string)*: Context for question, e.x. land management, research.
### Definitions

- <a id="%24defs/Answer"></a>**`Answer`** *(object)*
  - **`eco_context`**: Ecoregion answer applies to.
    - **All of**
      - : Refer to *[EcoContext](#%24defs/EcoContext)*.
  - **`case_studies`**: The case studies to which the question applies.
    - **All of**
      - : Refer to *[CaseStudy](#%24defs/CaseStudy)*.
  - **`data_inputs`** *(array, required)*: The science inputs to which the question applies.
    - **Items**: Refer to *[DataProduct](#%24defs/DataProduct)*.
  - **`processing_methods`** *(array, required)*: How to process data inputs.
    - **Items**: Refer to *[ProcessingMethod](#%24defs/ProcessingMethod)*.
- <a id="%24defs/CaseStudy"></a>**`CaseStudy`** *(object)*
  - **`name`** *(string, required)*: The name of the case study.
  - **`description`** *(string, required)*: A description of the case study.
  - **`reference`**: Reference for the case study.
    - **Any of**
      - : Refer to *[ReferenceModel](#%24defs/ReferenceModel)*.
      - *null*
- <a id="%24defs/DataProduct"></a>**`DataProduct`** *(object)*
  - **`name`** *(string, required)*: The name of the science input.
  - **`description`** *(string, required)*: A description of the science input.
  - **`science_input`**: The name of the science input. Default: `null`.
    - **Any of**
      - *string*
      - *null*
  - **`reference`** *(array, required)*: The reference model for the science input.
    - **Items**: Refer to *[ReferenceModel](#%24defs/ReferenceModel)*.
  - **`data_source`** *(array, required)*: Where this data comes from.
    - **Items**: Refer to *[DataSource](#%24defs/DataSource)*.
  - **`processing_methods`** *(array, required)*: How to process data inputs.
    - **Items**: Refer to *[ProcessingMethod](#%24defs/ProcessingMethod)*.
- <a id="%24defs/DataSource"></a>**`DataSource`** *(object)*
  - **`name`** *(string, required)*: The name of the data source.
  - **`platform_type`** *(string, required)*: Platform type (satellite, ground sensor, etc.
  - **`references`** *(array, required)*: References describing the source.
    - **Items**: Refer to *[ReferenceModel](#%24defs/ReferenceModel)*.
- <a id="%24defs/EcoContext"></a>**`EcoContext`** *(object)*
  - **`region`** *(string, required)*: Region answer applies to.
  - **`ecosystem`** *(string, required)*: Ecosystem answer applies to.
  - **`weather`** *(string, required)*: Weather answer applies to.
- <a id="%24defs/ProcessingMethod"></a>**`ProcessingMethod`** *(object)*
  - **`name`** *(string, required)*: Name of the processing method.
  - **`reference`** *(array, required)*: The reference model for the science input.
    - **Items**: Refer to *[ReferenceModel](#%24defs/ReferenceModel)*.
- <a id="%24defs/ReferenceModel"></a>**`ReferenceModel`** *(object)*
  - **`name`** *(string, required)*: The name of the reference.
  - **`description`** *(string, required)*: A description of the reference model.
  - **`url`**: URL for reference. Default: `null`.
    - **Any of**
      - *string*
      - *null*
  - **`citation`**: citations. Default: `null`.
    - **Any of**
      - *array*
        - **Items** *(string)*
      - *null*

