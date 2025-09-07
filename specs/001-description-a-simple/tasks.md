# Tasks: QnA App for PDFs

**Input**: Design documents from `/specs/001-description-a-simple/`
**Prerequisites**: plan.md (required)

## Execution Flow (main)

```plaintext
1. Load plan.md from feature directory
   → Extract: tech stack, libraries, structure
2. Generate tasks by category:
   → Setup: project init, dependencies, linting
   → Tests: contract tests, integration tests
   → Core: models, services, endpoints
   → Integration: DB, middleware, logging
   → Polish: unit tests, performance, docs
3. Apply task rules:
   → Different files = mark [P] for parallel
   → Same file = sequential (no [P])
   → Tests before implementation (TDD)
4. Number tasks sequentially (T001, T002...)
5. Validate task completeness:
   → All contracts have tests?
   → All entities have models?
   → All endpoints implemented?
6. Return: SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Phase 3.1: Setup

- [ ] T001 Create project structure for backend and frontend

- [ ] T002 Initialize Python project with FastAPI and Streamlit dependencies

- [ ] T003 [P] Configure linting and formatting tools (e.g., black, flake8)

- [ ] T004 [P] Add Makefile to set up Qdrant container instance via Docker

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3

### CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation

- [ ] T005 [P] Contract test POST /api/upload in backend/tests/contract/test_upload_post.py

- [ ] T006 [P] Contract test POST /api/qna in backend/tests/contract/test_qna_post.py

- [ ] T007 [P] Integration test file upload in backend/tests/integration/test_file_upload.py

- [ ] T008 [P] Integration test QnA flow in backend/tests/integration/test_qna_flow.py

- [ ] T009 [P] Integration test summarization flow in backend/tests/integration/test_summary_flow.py

## Phase 3.3: Core Implementation (ONLY after tests are failing)

- [ ] T010 [P] Implement file upload endpoint in backend/src/api/upload.py

- [ ] T011 [P] Implement QnA and summarization endpoint in backend/src/api/qna.py

- [ ] T012 [P] Integrate DSPY for LLM calls to Ollama in backend/src/services/llm_service.py

- [ ] T013 [P] Implement RAG pipeline with Qdrant in backend/src/services/rag_service.py

- [ ] T014 [P] Create Streamlit UI for file upload and chat in frontend/src/app.py

## Phase 3.4: Integration

- [ ] T015 Connect backend to Qdrant instance

- [ ] T016 Add middleware for logging and error handling

- [ ] T017 Add CORS and security headers to backend

- [ ] T018 Integrate Streamlit UI with backend API

## Phase 3.5: Polish

- [ ] T019 [P] Unit tests for DSPY integration in backend/tests/unit/test_llm_service.py

- [ ] T020 [P] Unit tests for RAG pipeline in backend/tests/unit/test_rag_service.py

- [ ] T021 [P] Performance tests for endpoints (<200ms response time)

- [ ] T022 [P] Update API documentation in backend/docs/api.md

- [ ] T023 [P] Update user guide for Streamlit UI in frontend/docs/user_guide.md

## Dependencies

- Tests (T005-T009) before implementation (T010-T014)

- T010 blocks T015, T018

- T013 blocks T015

- Implementation before polish (T019-T023)

## Parallel Example

```plaintext
# Launch T005-T009 together:
Task: "Contract test POST /api/upload in backend/tests/contract/test_upload_post.py"
Task: "Contract test POST /api/qna in backend/tests/contract/test_qna_post.py"
Task: "Integration test file upload in backend/tests/integration/test_file_upload.py"
Task: "Integration test QnA flow in backend/tests/integration/test_qna_flow.py"
Task: "Integration test summarization flow in backend/tests/integration/test_summary_flow.py"
```
