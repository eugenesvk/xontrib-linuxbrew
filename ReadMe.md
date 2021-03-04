<p align="center">
Add Homebrew's shell environment to <a href="https://xon.sh">xonsh shell</a> on Linux
<br/>
(alternative to <a href="https://docs.brew.sh/Homebrew-on-Linux">shellenv</a>)
</p>

<p align="center">  
If you like the idea, ask Homebrew to implement it natively as my <a href="https://github.com/Homebrew/brew/pull/10757">fix</a> was rejected because “xonsh is far too niche”
</p>

## Introduction

Homebrew has a `shellenv` command to add __Homebrew__ environment to your shell: it adds a few
environment variables (`HOMEBREW_` `PREFIX`/`CELLAR`/`REPOSITORY`) and updates a few paths (`MAN`/`INFO`/ `PATH`). Unfortunately it doesn't support __xonsh__ shell, and the devs are not yet willing to [fix it](https://github.com/Homebrew/brew/pull/10757), requiring adding the environment variables manually...

Or using this xontrib, which automatically translates the default __bash__ output of `shellenv` into __xonsh__

## Installation

To install use pip:

```bash
xpip install xontrib-linuxbrew
# or: xpip install -U git+https://github.com/eugenesvk/xontrib-linuxbrew
```

## Usage

Add this to your xonsh shell profile script at `~/.xonshrc` or `~/.config/rc.xsh`
```bash
xontrib load linuxbrew
```

Set level of verbosity via `$XONTRIB_LINUXBREW_LOGLEVEL` to __0–3__:

  - 0 print nothing (fail silently)
  - 1 (default) print errors (e.g. can't find brew at default locations)
  - 2 print warnings (e.g parsing errors)
  - 3 print more verbose messages

## Known issues

- Only default installation paths (`~/.linuxbrew` and `/home/linuxbrew/.linuxbrew`) are supported

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
