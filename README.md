# askkkpy
Simple REPL for communication with a TCP server using the console

## Example: connect to and communicate with [kavakava](https://github.com/bsoptei/kavakava)

```p
askkkpy:update John Doe;42;
b'OK'
askkkpy:update Big Oak Tree;420;
b'OK'
askkkpy:bykeys John Doe;
b'{"John Doe": "42"}'
askkkpy:byvals 420;
b'{"Big Oak Tree": "420"}'
askkkpy:
```
