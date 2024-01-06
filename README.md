# C-to-HTML
Contém um programa que recebe um arquivo .c ou .h e torna-o pronto para ser copiado e colado num arquivo HTML, sem perda de formatação.
O programa converte todos os "<" para "\&lt;" e todos os ">" para "\&gt;", de modo que estes símbolos não sejam confundidos com tags HTML.
Além disso, o programa adiciona tags <code class="coment"> envolvendo quaisquer tipos de comentário. Um arquivo new_file.txt é retornado
contendo o código formatado.
Este programa foi desenvolvido para automatizar a formatação de códigos C para um formato amigável ao HTML durante a criação de um site
com tutoriais de C.
