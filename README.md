# Development Log

## v0.1

### ✔ Image Ingestion Pipeline

Completed the first iteration of the MediaVault backend.

Implemented:

- Local image import
- URL downloads
- Validation
- Thumbnail generation
- Metadata extraction
- SQLite persistence

Architecture:

Vault
→ Downloader
→ Processor
→ Database


## v0.2.0
- added aspect ratio algorithm
- cleaned up Database code a bit
- fixed some faulty Datatype declarations
### Clean Up Work

