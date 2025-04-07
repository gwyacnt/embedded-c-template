# embedded-c-template

Embedded C template repo

## Features

- **Modular Structure**: Components are organized into separate folders with `include`, `src`, and `test` subdirectories.
- **CMake Build System**: Simplifies building, testing, and managing dependencies.
- **Unit Testing**: Integrated with Google Test for C++ to ensure code reliability.
- **GitHub Actions**: Automated build and test workflows.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- GCC or Clang
- CMake (version 3.10 or higher)
- Google Test (for unit testing)

### Building the Project

1. Clone the repository:
   ```
   git clone https://github.com/your-username/embedded-c-template.git
   cd embedded-c-template
   ```
2. Create a build directory and compile the project
    ```
    cmake -S . -B build
    cmake --build build
    ```

### Running the Application
After building, you can run the main application:
```
./build/main
```

### Running Tests
To execute unit tests:
~~~
cd build
ctest --output-on-failure
~~~

### Contributing
Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes and push them to your fork.
- Submit a pull request.

### License
This project is licensed under the MIT License. 

### Contact
For questions or feedback, feel free to open an issue or contact the repository owner.