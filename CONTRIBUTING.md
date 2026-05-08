# Contributing

Open source projects shine when anyone can contribute, and this project is no different. However, there are some guidelines
to adhere to in order to get your contribution merged in. In general, if you adhere to the Django contributing
guidelines, all is well: https://docs.djangoproject.com/en/dev/internals/contributing/

## Setup

1. Fork the repository in GitHub and then clone it:

  ```
  git clone git@github.com:<your-gh-username>/django-choices-2.git
  ```

2. Optional: Install `uv` if not installed

  ```
  pip install uv
  ```

3. Create the virtual environment and install dependencies:

  ```
  uv sync --dev
  ```

4. Activate the virtual environment:

  ```
  source .ven/bin/activate
  ```

## Tests

All changes should be accompanied by a test that either tests the new behaviorr, or tests the regression. Make sure all the tests still pass after your changes - for your current Django and Python version this can be done by running:

```
python -m runtests
```

And to run the entire matrix of Django and Python versions using tox-uv:

```
tox
```

## Documentation

When behavior changes or gets added, check whether the documentation needs updates. If so, please submit a draft or final version.

## Pull requests

When you think the patch is ready, submit a pull request to the `develop` branch. If it's a bug fix, the maintainer(s) will take care of bumping the version and uploading to PyPI. Feel free to add yourself to the CONTRIBUTORS.md file.

## Smaller style guidelines

### Commit(s)

Try to keep commits as atomic as possible. It's fine to do many small commits before submitting the PR,
you can always rebase your branch to make a nice commit history. A commit that adds the test, and
then a different commit that fixes the issue/feature is reasonable, combining them is fine as well.

### Code style

* Stick to PEP8, with the exclusion of the 80-char max line length. 80 columns is a guideline, 120 is the
  upper limit.
* Use 4 spaces instead of tabs.
* Follow https://docs.djangoproject.com/en/1.9/internals/contributing/writing-code/coding-style/
