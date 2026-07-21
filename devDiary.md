

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
> [] get the pipeline working again
> [] refactor Processor into abstract Class
> [] refactor Asset class into something that can spit out its data
> [x] implement file hashing
### Implemented
> File hashing
>   - the processor now spits out file_hashes and they're stored in the database, also my tests based on repeatedly throwing the same image
>     database are now unfunctional
### Learned
>
### Problems encountered
>
### Tomorrow
>
### Biggest takeaway
>
### Commits
>
### Project State
>
---