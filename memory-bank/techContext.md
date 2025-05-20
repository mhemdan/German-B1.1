# Technical Context

## Technologies Used

### File Formats
- **CSV (Comma-Separated Values)**
  - Used for vocabulary lists
  - Compatible with Anki import
  - Simple two-column format (German and English)

- **Markdown (.md)**
  - Used for formatted content with rich features
  - Supports headings, tables, code blocks, and emoji
  - Compatible with various platforms including Notion
  - Allows for structured, readable content

### Tools & Platforms
- **Anki**
  - Spaced repetition flashcard system
  - Primary end-use platform for vocabulary memorization
  - Imports CSV files for flashcard creation

- **Notion**
  - Knowledge management platform
  - Used for organizing and structuring content
  - Exports to various formats including CSV and Markdown
  - Supports tables, databases, and rich formatting

- **Text Editors**
  - Used for creating and editing Markdown files
  - Support for syntax highlighting and preview

## Development Setup
- Text editor with Markdown support
- CSV editor or spreadsheet software
- Anki for testing imported flashcards
- Notion for content organization and management

## Technical Constraints
- CSV files must maintain proper formatting for Anki import
- Markdown files should be compatible with both GitHub and Notion rendering
- Special characters and formatting in German language must be preserved
- File naming must be consistent for proper organization

## Dependencies
- Anki for flashcard usage
- Notion for content management (optional)
- Text editor for file creation and editing
- Web browser for accessing online resources

## Technical Workflow
1. Create or update content in appropriate format (CSV or Markdown)
2. Organize files according to naming conventions
3. Test import into Anki (for CSV files)
4. Review rendering in Markdown viewers
5. Backup files regularly

## Technical Considerations
- Ensure proper encoding (UTF-8) to support German special characters
- Maintain consistent formatting across files
- Follow established patterns for new content creation
- Consider compatibility with mobile devices for on-the-go learning
