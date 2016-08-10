// http://stackoverflow.com/questions/4358383/c-scanf-with-spaces-problem
// scanf stops reading from space with space.
// to read until the first newline:
scanf("%[^\n]", bookname);
// read max 29 chars until newline
scanf("%29[^\n]", bookname);
//or simply use
fgets(bookname, sizeof bookname, stdin);
