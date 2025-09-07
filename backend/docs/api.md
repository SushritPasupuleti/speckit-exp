# API Documentation

## Endpoints

### POST /api/upload

- **Description**: Upload a PDF file.

- **Request**:
  - `file`: PDF file to upload.

- **Response**:
  - `file_id`: Unique identifier for the uploaded file.

### POST /api/qna

- **Description**: Ask a question about an uploaded PDF.

- **Request**:
  - `file_id`: ID of the uploaded file.
  - `question`: Question to ask.

- **Response**:
  - `answer`: Generated answer to the question.
