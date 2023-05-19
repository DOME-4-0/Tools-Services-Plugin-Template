# Tools-Services-Plugin-Template
This is a template for a wrapper that will allow third-party tools and services
to consume data from the DOME 4.0 platform, perform some functionality, and return 
relevant data back to DOME 4.0 to the benefit of the platform's users. 

The template has been created using [cookiecutter](https://github.com/cookiecutter/cookiecutter). 

## Generate your project from the template
First, install cookiecutter according to [the documentation](https://cookiecutter.readthedocs.io/en/latest/installation.html).

Then run the following command to generate your project:
```
cookiecutter gh:DOME-4-0/Tools-Services-Plugin-Template
```

Now type in the required inputs to customize your repository.

Alternatively, you can pre-define the inputs in a JSON file and pass it to the cookiecutter command using the --config-file option. The list of input keys and default values can be found in cookiecutter.json.
An overview is also provided in the following table:

| Input key | Description | Default value |
|:---:|:--- |:--- |
| `project_name` | A human-readable name of the project. | `My DOME 4.0 tool` |
| `project_slug` | The official package name to be used when installing the package via a package manager (e.g., `pip` or `conda`).<br>This will be the root directory name and should also be the repository name on an online git repository (like GitHub or GitLab).<br><br>**Important**: A project slug value may *not* include white space. | `my-dome40-tool` |
| `package_name` | The Python importable root module.<br>This will be the root module repository name, under which the source code will be placed.<br><br>**Important**: A package name value may *not* include white space. A package name value may *only* be made up of the character set: a-z, A-Z, `_`, 0-9, and may *not* start with a number. | `my_dome40_tool` |
| `author` | The author of the package. This can also be your organization name. | `Firstname Lastname` |
| `organization` | Your organization. | `DOME 4.0` |
| `email` | The author's email address. | `firstname.lastname@SINTEF.org` |
| `version` | Start version.<br><br>**Important**: Must follow semantic versioning. For more information see [semver.org](https://semver.org). | `0.0.1` |
| `year` | The current year. | `2023` |
| `use_git` | Whether or not the generated repository should be initialized using [`git`](https://git-scm.com). | `True` |
| `username` | A public source code platform username, e.g., for [GitHub](https://github.com), [GitLab](https://gitlab.com), [BitBucket](https://bitbucket.org) | `GitHub_GitLab_BitBucket_etc_Username` |
| `scm_url` | The intended or existing URL to the repository's source code. | `https://github.com/FirstnameLastname/my-dome40-tool` |
