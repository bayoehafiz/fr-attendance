# Face Recognition Simple Project

This project is a Python-based face recognition system that uses machine learning algorithms to identify and verify faces in images.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/face-recognition.git
    ```
2. Navigate to the project directory:
    ```bash
    cd face-recognition
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the face recognition script on an image:
```bash
python main.py
```
And follow the onscreen prompt

## Features

- Detect faces captured via webcam.
- Recognize and label known faces based on photo data inside folder `faces`.
- High accuracy and performance using state-of-the-art machine learning models.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.