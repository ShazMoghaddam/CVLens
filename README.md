# CVLens

CVLens is a Python-based AI CV reader and analyser designed to parse resumes (PDF and DOCX), extract structured information, and generate actionable feedback on CV quality. The project focuses on automating common CV screening and review tasks, making it useful for early-stage recruitment analysis, personal CV improvement, and as a portfolio project demonstrating applied NLP and document processing.

---

## Features

* 📄 **Multi-format CV parsing**: Supports both PDF and DOCX resumes
* 🧠 **NLP-powered analysis**: Uses spaCy for text processing and skill extraction
* 🧩 **Section detection**: Identifies common CV sections (e.g. Experience, Education, Skills)
* 🛠 **Skill extraction**: Extracts and normalises skills from unstructured text
* ✅ **Quality checks**: Flags potential CV issues (missing sections, weak structure, etc.)
* 📝 **Feedback generation**: Produces readable feedback based on analysis results

---

## Project Structure

```
CVLens/
│
├── main.py                 # Entry point for running the CV analysis
├── parser.py               # Handles PDF and DOCX text extraction
├── section_detector.py     # Detects and labels CV sections
├── skills_extractor.py     # Extracts skills using NLP and pattern matching
├── quality_checks.py       # Performs CV quality and completeness checks
├── feedback_generator.py   # Generates human-readable feedback
│
├── data/
│   └── sample_resume.pdf   # Example CV for testing
│
└── README.md
```

---

## Technologies Used

* **Python 3**
* **spaCy** – Natural Language Processing
* **pdfplumber** – PDF text extraction
* **python-docx** – DOCX file handling
* **xml.dom.minidom** – Structured document handling
* **re** – Text pattern matching
* **os** – File system operations

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/CVLens.git
cd CVLens
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\\Scripts\\activate     # Windows
```

3. Install dependencies:

```bash
pip install pdfplumber python-docx spacy
```

4. Download a spaCy language model:

```bash
python -m spacy download en_core_web_sm
```

---

## Usage

Place a CV file (PDF or DOCX) inside the `data/` folder and run:

```bash
python main.py
```

The script will:

1. Parse the CV
2. Detect sections
3. Extract skills
4. Run quality checks
5. Generate feedback in the console output

---

## Example Use Cases

* Analysing your own CV before job applications
* Automating CV pre-screening logic
* Demonstrating NLP, text parsing, and modular Python design
* Extending into a web app or recruitment tool

---

## Future Improvements

* Add scoring or ranking system
* Support more CV formats
* Export feedback to a report (PDF/JSON)
* Integrate with a web interface (e.g. Flask or FastAPI)
* Expand skill taxonomy and role-specific analysis

---

## Disclaimer

CVLens is a learning and portfolio project and should not be used as a sole decision-making tool for recruitment.

---

## Author

Developed as a Python and Data Science portfolio project.

Feel free to explore, fork, and extend the project.
