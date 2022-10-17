# INTRO

![terminalexample](/example1.PNG)


>This is a quick installation guide including references for my WSL terminal.  
>I have included the zshrcconfig which contains my personal setting and alias that I'm using with my WSL.  
>Rename the file to **```zshrcconfig -> .zshrc```**.

# SETUP

## ZSH

### install

```bash
sudo apt-get install zsh -y
```

## Oh-my-ZSH

### install

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

 reference: <https://github.com/ohmyzsh/ohmyzsh/wiki>

---

## PowerleveL10k

### Install

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

```bash
### Update theme in ~/.zshrc
ZSH_THEME="powerlevel10k/powerlevel10k"
```

reference: <https://github.com/romkatv/powerlevel10k>

---

### zsh-syntax-highlighting

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

```bash
#update plugins in ~/.zshrc
plugins=(
...
zsh-syntax-highligting
)
```

---

### zsh-autosuggestions

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

```bash
#update plugins in ~/.zshrc
plugings=(
...
zsh-autosuggestions
)
```

---

## exa - modern ls replacement

### Installing environment dependencies

```bash
#requires: rust
#dependencies: libgit2 and cmake

###installing rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
####Import the environment config for rust
source $HOME/.cargo/env
rustc --version

###installing libgit2
sudo apt-get install libgit2-dev -y

###installing cmake
sudo apt-get install cmake -y
```

### Installing exa

```bash
#installing and adding to $PATH
cargo install exa

# OR 

scp ./target/release/exa /usr/bin/
```

Setting "persistent" alias in shell

```bash
#add alias to ~/.zshrc
alias ls="exa --icons"
```

references:

<https://the.exa.website/install/source>

<https://www.rust-lang.org/tools/install>

---

## Fuzzy File Finding

### Installing fuzzy file finding

```bash
#Cloning repository and installing
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

```bash
#update plugins in ~/.zshrc
plugings=(
...
fzf
)
```

reference:

---

## bat - modern cat replacement

```bash
sudo apt install bat
```

Coloring manpages

```bash
#add export to ~/.zshrc
#colorizing man pages with
export MANPAGER="sh -c 'col -bx | batcat -l man -p'"

```

< Setting "persistent" alias in shell

```bash
#add alias to ~/.zshrc
alias bat="batcat"
```
