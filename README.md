# Coreutils-EYAD_HUSSEIN

Coreutils-EYAD_HUSSEIN is a collection of Unix-like command line utilities implemented in Python.

## Project Structure

```bash
.
├── README.md
└── src
    └── Coreutils-EYAD_HUSSEIN-python
        ├── cat.py
        ├── echo.py
        ├── env.py
        ├── false.py
        ├── head.py
        ├── __init__.py
        ├── tail.py
        ├── tree.py
        ├── true.py
        ├── wc.py
        └── yes.py
```

- **src/**: Source directory for the project.
- **src/Coreutils-EYAD_HUSSEIN-python/**: Holds commands files.

## Commands Implemented

- **cat**: Concatenate files and print on the standard output.

  - Allowed flags: `-n` flag to number output lines.

- **echo**: Display line of text in standard output.

  - Allowed flags: `-n` flag to omit the trailing newline.

- **env**: List all environment variables.

  - No additional flags allowed.

- **false**: Do nothing, unsuccessfully.

  - No additional flags allowed.

- **head**: Output the first part of files.

  - Allowed flags: `-n` flag to specify the number of lines to print.

- **tail**: Output the last part of files.

  - Allowed flags: `-n` flag to specify the number of lines to print.

- **tree**: List contents of directories in a tree-like format.

  - Allowed flags: `-L` to list the deepest level to list directories' contents'

- **true**: Do nothing, successfully.

  - No additional flags allowed.

- **wc**: Print newline, word, and byte counts for each file.

  - Allowed flags: `-l`, `-w`, `-c` flags to display only lines, words, or characters respectively.

- **yes**: Output a string repeatedly until killed.
  - No additional flags allowed.

## Getting Started

### Installation

Clone the repository and navigate to `src/Coreutils-EYAD_HUSSEIN-python`.

### Building Commands

You can run each command separately. Below are the instructions for using each command.

#### cat

**Usage**:

```bash
python3 cat.py [flags] <file>...
```

#### echo

**Usage**:

```bash
python3 echo.py [flags] <text>...
```

#### env

**Usage**:

```bash
python3 env.py
```

#### false

**Usage**:

```bash
python3 false.py
```

#### head

**Usage**:

```bash
python3 head.py [flags] <file>...
```

#### tail

**Usage**:

```bash
python3 tail.py [flags] <file>...
```

#### tree

**Usage**:

```bash
python3 tree.py [flags] <directory>
```

#### true

**Usage**:

```bash
python3 true.py
```

#### wc

**Usage**:

```bash
python3 wc.py [flags] <file>...
```

#### yes

**Usage**:

```bash
python3 yes.py [text]
```

### Usage

Execute commands using the file for each specific command.

```bash
python3 <command>.py [flags] (arg || [<args list>])
```

## Examples

- Print the first 10 lines of a file:

  ```bash
  python3 head.py -n 10 myfile.txt
  ```

- Print the last 10 lines of a file:
  ```bash
  python3 tail.py -n 10 myfile.txt
  ```
