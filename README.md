# **INTRO**

>This is a quick installation guide including references for my WSL terminal. Installation my vary depending on shell and OS.  
>I have shifted themes from **```PowerLevel10k -> Starship.rs```**  
>and I have included the starship.toml file which holds my current prompt config.  
>**```cp starship.toml to ~/.config```**  
>I have included the zshrcconfig which contains my personal settings and aliases that I'm using with my WSL.  
>Rename the file to **```zshrcconfig -> .zshrc```** and move it to ```/~```.  

## **ZSH Prompt**

### **ZSH**

#### ***install***

```bash
sudo apt-get install zsh -y
```

### **Oh-my-ZSH**

#### ***install***

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

reference: <https://github.com/ohmyzsh/ohmyzsh/wiki>

---
  
# **Theme**  

### **Starship.rs**

#### ***Install***

```bash
curl -sS https://starship.rs/install.sh | sh
```

Add the following to the end of ``~./zshrc``

```zsh
eval "$(starship init zsh)"
```

![terminalexampleSh](/terminalexampleStarship.PNG)

reference: <https://Starship.rs>

---

### **PowerleveL10k**

#### ***Install***

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

```bash
### Update theme in ~/.zshrc
ZSH_THEME="powerlevel10k/powerlevel10k"
```

![terminalexamplep10k](/example1.PNG)

reference: <https://github.com/romkatv/powerlevel10k>


---

# Modules

---

## ***zsh-syntax-highlighting***

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

## ***zsh-autosuggestions***

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

## **exa - Modern ls replacement**

> This method of installation is only required IF using Windows or WSL.  
> For Mac or Linux use cmd below  
```sudo apt-get install exa```

#### ***Installing environment dependencies***

```zsh
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

#### ***Installing exa***

```zsh
# using Rust to install and add exa to $PATH
cargo install exa

# OR Building from source and adding tp $PATH.

git clone https://github.com/ogham/exa.git ##pull source from github

cargo build --release ## build  exa from the source code with Rust.

scp ./target/release/exa /usr/bin/ # copy the executable to $PATH
```

Setting "persistent" alias in shell

```zsh
#add alias to ~/.zshrc
alias ls="exa --icons"
```

references:

<https://the.exa.website/install/source>

<https://www.rust-lang.org/tools/install>

---

## **Fuzzy File Finding**

#### ***Installing fuzzy file finding***

```zsh
#Cloning repository and installing
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

```zsh
#update plugins in ~/.zshrc
plugings=(
...
fzf
)
```

reference:

---

## **bat - Modern cat replacement**

#### ***Installing bat***

```bash
sudo apt install bat
```

Coloring manpages

```bash
#add export to ~/.zshrc
#colorizing man pages with batcat
export MANPAGER="sh -c 'col -bx | batcat -l man -p'"

```

Setting "persistent" alias in shell

```bash
#add alias to ~/.zshrc
alias bat="batcat"
```
