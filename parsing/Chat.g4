grammar Chat;

// parser

chat: line EOF;
line: name command msg Newline;
name: Word Whitespace;
command: Word ':' Whitespace;
mention: '@' Word;
msg: (Word | mention | Whitespace)+;

// lexer
fragment Lowercase: [a-z];
fragment Uppercase: [A-Z];

Word: (Lowercase | Uppercase | '_')+;
Newline: ('\r' | '\n')+;
Whitespace: ('\t' | ' ');