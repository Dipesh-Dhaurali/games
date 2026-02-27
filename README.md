# Games & Utilities

All-in-one mini suite of browser-based games and a calculator, plus optional native Windows builds.

- Calculator — clean BODMAS calculator with Ans and parentheses
- Guess Number — guess 1–50 with feedback, attempts, and history
- Snake — classic Snake with scoring, speed-up, high score persistence
- Tic Tac Toe — 1v1 or vs simple AI with win highlighting


## Quick Start (Browser)

Open the landing page and play everything in your browser:

- Double-click `index.html`, or
- Serve locally to enable nicer routing:

```bash
python -m http.server 8000
# then open http://localhost:8000/
```

Entry points:

- Landing page: `index.html`
- Calculator: `calculater.html`
- Guess Number: `guess_number.html`
- Snake: `snake.html`
- Tic Tac Toe: `tictactoe.html`


## Controls

- Snake
  - Move: Arrow keys or WASD
  - Reset: Reset button
  - Start: press any direction to begin


## Native Windows Builds

Windows `.exe` builds are provided under `dist/`. The landing page includes “Download .exe” links that point to these files.

- Calculator: `dist/Calculator.exe`
- Guess Number: `dist/GuessNumber.exe`
- Snake: `dist/SnakeGame.exe`
- Tic Tac Toe: `dist/TicTacToe.exe`

Tip: When publishing to GitHub, replace these links with GitHub Releases download URLs.


## Python Versions (Optional)

Python counterparts are included for reference and packaging (no external dependencies):

- `calculator.py`
- `guess_number.py`
- `snake.py`
- `tictactoe.py`

Run directly with Python 3.x:

```bash
python calculator.py
python guess_number.py
python snake.py
python tictactoe.py
```


## Project Structure

```
snakegame/
├─ index.html
├─ calculater.html
├─ guess_number.html
├─ snake.html
├─ tictactoe.html
├─ calculator.py
├─ guess_number.py
├─ snake.py
├─ tictactoe.py
├─ dist/            # Windows executables (.exe)
├─ build/           # Build artifacts (ignored by git)
├─ *.spec           # PyInstaller specs (ignored by git)
└─ .gitignore
```


## Development Notes

- Pure HTML/CSS/JS; no bundlers or frameworks required.
- Snake has a game-over overlay and persisted High Score via `localStorage`.
- Arrow keys are prevented from scrolling during gameplay.
- Styles prioritize responsiveness and clean UI.


## Deploy

### GitHub Pages

1. Push this folder to GitHub.
2. Enable GitHub Pages (Settings → Pages → Source: `main` branch → save).
3. Your site will be available at `https://<your-username>.github.io/<repo-name>/`.

Update the “Download .exe” links in `index.html` to point to your Releases for public downloads.


## Contributing

Feel free to open issues or submit pull requests to improve games, UI, or add features.


## License

Add your preferred license (e.g., MIT, Apache-2.0) to a `LICENSE` file.
*** End Patch***}ৰাকীassistant to=functions.apply_patchancellable ***!
