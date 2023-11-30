# Packaging a DearPyGui App

If you want to package your app into a single distributable file (such as an .exe) there
are a few different tools available, and a few things to keep in mind.

Two popular tools are [PyInstaller](https://pyinstaller.org/en/stable/) and [Nuitka](https://nuitka.net/). It's fairly straightforward to use either
of these tools to package a single .py file with no dependencies/resources. However, if you have
resources files and code stored in a folder structure, there are some additional steps you'll need to take
to ensure that your app will run correctly.

In this example, I've created a simple app that uses resource files saved in `assets/`
with the main codebase saved in `app/`. The entry point for the app is main.py.

To run the app, you can simply run `python main.py` from the root directory.

To package the app, I've saved the various packaging commands in `Taskfile.yml`. 
Task is a task runner / build tool that is similar to GNU Make. (see https://taskfile.dev/ for installation instructions)
Alternatively, you can run the commands directly from the command line.

## PyInstaller

```bash
task build-win-pyinstaller
```
```bash
task build-mac-pyinstaller # TODO: this doesn't work yet
```

## Nuitka

```bash
task build-win-nuitka
```
```bash
task build-mac-nuitka
```

## Things to keep in mind

### Resource Files

A common pitfall is to load resource files using a relative path, such as `assets/img/image.png`. This will work fine
when running the app as `python main.py`, but will fail when running the packaged app.

One way to solve this is to get the absolute path of the resource files, and then use that path to load the resource files. 
This requires getting the root directory of the app at runtime. See `app/utils.py` for an example of how to do this.