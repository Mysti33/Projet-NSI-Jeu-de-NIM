def game_mode() -> int:
    mode = int(input("Mode de jeux | 1. JcJ / 2. JcO [1/2] : "))
    while mode != 1 and mode != 2:
        mode = int(input("Mode de jeux | 1. JcJ / 2. JcO [1/2] : "))
    return(mode)