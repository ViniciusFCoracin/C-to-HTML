# Esse programa recebe um arquivo .c ou .h e cria um novo arquivo,
# new_file.txt, com formatação html (isto é, troca < por &lt; e 
# > por &rt;), além de adicionar uma tag <code class="coment"> 
# envolvendo comentários.


def main():
    path = input()
    with open("new_file.txt", "w") as new_file:
        with open(path, "r") as file:
            while (True):
                char = file.read(1)
                if char == "<":
                    new_file.write("&lt;")
                elif char == ">":
                    new_file.write("&gt;")
                elif char == "/":
                    char = file.read(1)
                    # Se for o início de um comentário de uma linha
                    if char == "/":
                        new_file.write(f'<code class="coment">//')
                        char = file.read(1)
                        while char != "\n":
                            new_file.write(char)
                            char = file.read(1)
                        new_file.write("</code>\n")
                    # Se for o início de um comentário de múltiplas linhas
                    elif char == "*":
                        new_file.write(f'<code class="coment">/*')
                    # Se não for comentário
                    else:
                        new_file.write(f"/{char}")
                elif char == "*":
                    char = file.read(1)
                    # Se for o final de um comentário
                    if char == "/":
                        new_file.write(f'</code>*/')
                    # Se não for comentário
                    else:
                        new_file.write(f"*{char}")
                elif not char:
                    break
                else:
                    new_file.write(char)

if __name__ == "__main__":
    main()
