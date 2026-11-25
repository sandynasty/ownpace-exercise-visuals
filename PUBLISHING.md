# GitHub setup

1. Create a new **private** repository at https://github.com/new named `ownpace-exercise-dataset`. Leave README, license and gitignore initialization unchecked if using the CLI.
2. Extract the ZIP, open Terminal, and change into the extracted `ownpace-exercise-dataset` folder.
3. Run:

```sh
git init -b main
git add .
git commit -m "Add OWNPACE exercise dataset v0.1.0 candidate"
git remote add origin https://github.com/YOUR_USERNAME/ownpace-exercise-dataset.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your own GitHub login. Authenticate with GitHub CLI or your configured credential manager if prompted. Alternatively use GitHub Desktop: Add Local Repository, create the repository if needed, commit and publish privately. GitHub's web upload can be used in smaller batches, but preserve folders and include hidden files; CLI/Desktop is preferable for hundreds of assets.

Local catalog: double-click `index.html`, or run `python -m http.server 8000` and visit `http://localhost:8000/`.

After all rights and exercise QA reviews are resolved, choose licenses, update the README and version, then make the repository public if desired. For a public static catalog, use Settings → Pages → Deploy from a branch → main → /(root). The resulting site will be `https://YOUR_USERNAME.github.io/ownpace-exercise-dataset/`. A private repo does not automatically make a Pages site private; do not deploy the preview externally until cleared.

The static JSON endpoint will be `/exercises.json` relative to that site. Pin a Git tag or bundle assets locally for production stability.
