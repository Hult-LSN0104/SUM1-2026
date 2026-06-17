# Hultagram

Hultagram is a simple Instagram clone built with Flask. It allows users to create posts with images, view a chronological feed, like posts, and comment on them.

## Features

- Post creation with image uploads
- Chronological feed viewing
- Liking posts
- Commenting on posts
- Timestamp display (e.g., "2 hours ago")

## Project Structure

```
Hultagram/
│-- static/
│   ├── styles.css  # CSS styles
│-- templates/
│   ├── base.html  # Main layout template with navigation
│   ├── index.html  # Homepage showing all posts
│   ├── post_detail.html  # Detailed view of a single post
│   ├── create.html  # Form for creating new posts
│-- uploads/  # Stores uploaded images
│-- app.py  # Main Flask application
│-- photogram.db  # SQLite database (auto-created)
│-- requirements.txt  # Dependencies
│-- README.md  # Project documentation
```

## Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/hultagram.git
   cd hultagram
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```sh
   python app.py
   ```
   The application will start on `http://127.0.0.1:5000/`

5. **Test functionality**
   - Create several posts with different images
   - Add comments to posts
   - Like posts to verify functionality

## Database

- The SQLite database (`photogram.db`) is created automatically when the app is first run.
- It stores posts, comments, and likes.

## Contributing

Feel free to fork the repository and submit pull requests with improvements!

## License

This project is licensed under the MIT License.

