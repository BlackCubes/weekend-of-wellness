<p align="center">
  <img src="https://github.com/BlackCubes/weekend-of-wellness/assets/29642735/f3286caa-f735-420b-8e7c-edd8d0fb6f35" width="480px" height="auto" alt="Mobile App logo" />
</p>
<h1 align="center">Weekend of Wellness</h1>
<p align="center">
    <br>
    <a href="https://www.djangoproject.com/">
        <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
    </a>
    <br>
</p>
This is the repo for the Kingsburg Weekend of Wellness which utilizes the power of Django for server-side rendering.
<br/>

## Project Requirements

- Python `v3.12+`

## Project Setup

1. Clone this repo at your preferred location in your machine.
2. Have the correct Python version installed according to the **Project Requirements** section by either downloading from the official website ([python.org](https://www.python.org/)), or by using a python version management such as pyenv ([Github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)). For more information on how to install pyenv, here is a really good article from Real Python on how to do it: [Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/).
3. Create a virtual environment with `python -m venv venv` (or `python3 -m venv venv`) in the root project directory.
4. Activate your virtual environment with `source venv/bin/activate` on Mac/Linux, or `venv\Scripts\activate` on Windows.
5. Install the necessary packages with `pip install -r requirements.txt`.
6. Next, activate the environment variables, migrations, and Django server with `source entrypoint.sh`.

## Development

### Local Development

To work with the project directly, the development machine needs `python` installed.

### Development Server

Refer to the **Project Setup** on how to install and run the application. The application will automatically reload if any source files are changed.

### Versioning

When starting work on a new release version, increment `minor` version (`v0.0.1` -> `v0.1.0`), `major` version (`v0.0.1` -> `v1.0.0`), or `patch` (`v0.0.1` -> `v0.0.2`).

### Template Repository

This project is configured as a [template repository](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template#about-repository-templates). It creates one commit in the new project based on the template instead of the entire original boilerplate history.

#### Updating Code Owners

In the repository there should be a `.github` folder with a `CODEOWNERS` file inside. This file represents who the owners of the repository code are. When you clone this repo, or use it as a template for a new project, you need to update this file to represent the new owners (you and whomever may be on your project). Simply remove the current owners in the file, and replace them with you and your teamates! The syntax is simply:

```
@<github username>
```

Be sure to add the github usernames of all developers on your project. Now anytime a pull request is created, all codeowners are added as reviews automatically! It also becomes a reference point when the project is picked back up in the future. We can easily see who has the best context for the code even years down the line. For more information you can click this link:

[Github Codeowners](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/about-code-owners)

#### Updating Issue Templates

Currently, the issue templates may have some things you don't want or need in your new project. This can be anything from the tags being set, to the person assigned for each issue. Be sure to go to the settings for the repository, and click `Set up templates` to configure them in a way that suits your needs. For more information you can click this link:

[Setting up issue templates](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/configuring-issue-templates-for-your-repository)
