

### Future Goals
---
## High Priority
---

> SHA256 File Hashing
> More Database Functionality
 # Video file support
>   - that includes Youtube Link support for now, use yt-dlpt and pytube and ffmpeg
>   - working on this turns AssetFactory into a HIGH priority
>   - teach the processor how to process Video files, probably in a subclass/different class
>   - implement some Database functions for more detailes querying: return a list of ids when a title is searched e.g
> # AssetFactory
>   - letting a separate function handle Asset construction, turn Processor into a sole data-extraction machine
>   - place for ImageAsset, VideoAsset etc...
>   - handles the logic of which Asset to create
---
## Medium Priority
> Custom Logging, pretty printing with Rich and Rich-Gradient
> 
---
## Low Priority
> Support for inserting entire Folders
> Custom Exceptions
    
---
## UNSORTED





---



### Biggest takeaway
---
## Date
19.07.2026

### Goals
- [x] Create images_v4 table with updated values, and re-do schema.sql


### Implemented
> algorhithm that calculates aspect ratio, learning the Math and writing my first algorhithm took 2,5 hours of my life smh
> cleaned up Database.py a bit
> updated table and schema.sql
> aspect_ratio property in the Asset class is now consistent over the entire Pipeline
> placeholder for File_Hashes
### Learned
> surprisingly i re-learned SQL syntax
> some Math, especially common and lowest common multiple, to calculate Aspect Ratios
> some algorhithm logic without over-engineering it
> actually sat down and invented a solution to a problem, one day i'll share my notebook pages (i wont they're messy AF)
> SQLite only takes placeholder arguments for Values, 

### Problems encountered
> i hate math, or atleast Division screws with my head
> logical operation in the aspect ratio algorithm
> SPELLING ALGORITHM THIS WOULD BE SO MUCH EASIER IF I WROTE THE ENTIRE THING IN GERMAN  
### Tomorrow
> implement file_hashing for real
> Focus on Database functionality, search, queries etc.
> some more Frontend exercises

### Biggest takeaway
>i learned that many "find the best match" problems can be solved with a single pass by keeping track of the current best candidate. I also discovered that Python's
>float("inf") REPRESENTS INFINITY HOLY MOLY, and its a sentinel value i will learn what that is another time.

### Commits

>UPDATE:
<Google Gemini definition:
A sentinel value is a special programming marker that acts as a signal to terminate a loop or recursive algorithm. It represents an "out-of-band" condition (like the end of a dataset or user input) and must be carefully chosen so it is never confused with valid, processing-worthy data.Key Concepts & ExamplesUnbounded Loops: When an algorithm needs to process a sequence of unknown length, a sentinel value breaks the loop. For example, if you are calculating the average of positive exam scores, you might use -1 or the string "done" as a sentinel to stop data entry.Flag/Signal: It tells the program, "We've reached the end, stop asking for input or iterating through this array".Absence of Data: Many languages use sentinel values like null or None to indicate that a specific variable or list search is empty or uninitialized.>

### Project State
> MediaVault can now ingest Images from local files, or URLs, returning an Asset with all necessary data
> Aspect ratios of Images are now calculated by themselves and its fully implemented
---
### DATE
> 20.07.26
### Goals
> [x] implement MediaType detection in MediaDetector.py
> [x] start working on the new Processor class with abstract classes
### Implemented
> Processor as a base Abstract Class
> started re-factoring Processor into image_processor 
> Type detection for files
> Enum for type detection and scaleability
### Learned
> python-magic is literal magic
> some classes and function can be beautifully simple
> abstract classes rock
> i should sleep more
> Enums are super for constant values that dont need re-typing at everystep, and it protects from typos (i need this ALOT)
### Problems encountered
> large refactors aren't fun (jk i love coding <3)
> ImageProcessor, formerly knows as Processor requires alot of re-structuring
> Refactoring introduces ALOT of bugs, i will do some hard work on the processors tomorrow
### Tomorrow
> repair ingestion pipeline, finish processor refactor
### Biggest takeaway
> Abstract classes are a good exercise in polymorphism
### Commits
> yes
### Project State
> MediaVault now automatically detects a given FileType using python-magic. The processing architecture is now moving from image-specific to more media types
---
### DATE
>21.07.2026     
### Goals
> [x] get the pipeline working again
> [x] refactor Processor into abstract Class
> [x] refactor Asset class into something that can spit out its data
> [x] implement file hashing
### Implemented
> File hashing
>   - the processor now spits out file_hashes and they're stored in the database, also my tests based on repeatedly throwing the same image
>     database are now unfunctional
> ingestion pipeline is functional again, stronger than ever
> started organizing the project into folders to keep it a bit more neat, also the src folder would become too crowded at this point
> Structure for future implementations and refactors stands
### Learned
> SHA256 Hashing and file hashing
> sub folder structuring
> folder and storage structure for later use, everything really becomes easier once file hashing stands
> separating Responsibilities
### Problems encountered
> a singular "." in an import screwed the entire pipeline, 15 minutes i'll never get back
> Refactoring creates 15 insertion bugs, then a few ValueErrors, then it was just spitting out None for a few minutes lol
### Tomorrow
> implement AssetFactory
### Biggest takeaway
> File hashing fucking rocks
> a good structure pay off very well
> TODAY I GOT EVERYTHING DONE I PLANNED TO DO
### Commits
> yea
### Project State
> MediaVault now has a structure where future implementations are way easier
---

### DATE
> 220.07.2026
### Goals
> [x] implement AssetFactory into the Pipeline structure
> [x] if time is left, work on the repository (formerly known as Database) class for more query features
### Implemented
> AssetFactory is now part of of the construction and re-consctruction path
> Added proper MediaType serialization/deserialization between Python and SQLite.
> Updated database queries to work with the new AssetFactory architecture
> Fixed Several issues that the Refactor introduced, i'd say the refactor is like 80% done
> cleaned up ingest_file function inside Vault HEAVILY
### Learned
> i still have alot to learn, but i love this project so much
> Enums need to serialized before storing them in SQLite and re-serialized when using them (implement this into repository)
### Problems encountered
> Forgot to reconstruct MediaType from the database string before passing data into the AssetFactory.
> Had to update several repository functions after changing the construction flow.
> Spent some time tracking down small integration bugs left behind by the refactor.
### Tomorrow
>
### Biggest takeaway
>Today's work wasn't about adding new features—it was about making the architecture consistent. Every bug I fixed came from one place still using the old design. Once every layer followed the same pipeline again, everything started falling back into place.
### Commits
> 7ba7bcc
### Project State
> still mid refactor, but the architecture for future file types is getting close to finished
---

### DATE
>23.07.2026
### Goals
> [x] Make repository more solid, and remove old junk
> [x] started implementing and learning PyTest
### Implemented
> search by title function
> first test
### Learned
> SQL is painful
> pytest structure
### Problems encountered
> today was a bad day mentally, we'll continue tomorrow
> i swear to god imports will be the end of me
### Tomorrow
> more testing and some fun coding
### Biggest takeaway
> fuck it, we ball
### Commits
> None
### Project State
> MediaVault now tests if AssetFactory returns an actual ImageAsset2
---
> Testing is driving me insane, so i had ChatGPT write todays entry, because fuck it:
### DATE
> 26.07.2026
### Goals
>Learn the basics of pytest
>Write the first meaningful repository tests
>Fix project-wide import issues
>Better understand Python package structure
### Implemented
>Set up repository tests using temporary SQLite databases.
>Verified that the repository initializes a fresh database correctly.
>Wrote a repository test that inserts an asset and verifies that the returned data matches the stored values.
>Fixed multiple stale imports after the package refactor.
>Learned how package-relative and absolute imports work and cleaned up inconsistent import paths.
>Improved my understanding of Python tracebacks by following the import chain to locate the failing module instead of guessing.
### Learned
>A traceback should be read from the bottom up. The exception tells me what failed, while the stack above it tells me how execution reached that point.
>Refactoring package structures often exposes stale imports one by one, which is normal.
>A unit test should verify a component's contract rather than every line of code.
>Repository tests and AssetFactory tests should be separated so failures point directly to the broken component.
>Good tests reveal architectural decisions. One failed assertion highlighted that I need to decide what the repository's contract for file paths should be.
### Problems encountered
>pent a significant amount of time chasing import issues after reorganizing the project.
>Writing tests felt slow and repetitive because I was unsure what was actually worth testing.
>Ran into platform-specific path differences (/ vs \), which exposed an inconsistency in how file paths are represented.
### Tomorrow
>Decide on the repository contract for path handling and update the tests accordingly.
>Add one more meaningful repository test for duplicate hash handling.
>Commit the testing foundation.
>Return to feature development, with the downloader rewrite, URL ingestion improvements, or video support being the next priorities.
### Biggest takeaway
> These are my own words:
> i get why Testing exists, but learning it is currently definitly the most dull aspect of Software engineering,
> i didn't add any new flashy features, but the testing foundation definitly showed me some of the weaknesses in my project, it especially forced me
> to learn a lot about imports in Python and how the package system worked instead of relying on imports that happened to work#
> writing tests forces me to define contracts between my components
> i also learned abit of probabilities and weighted loot tables when i was distracting myself on a different project
### Commits
>
### Project State
>MediaVault now has a functioning testing foundation. The repository is no longer completely unverified, pytest is integrated into the workflow, and the project structure is much cleaner after resolving the import issues. Future refactors should be significantly less risky.
---