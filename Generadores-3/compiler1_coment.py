from perfil import profile1,timethis
import logging
logging.basicConfig(level=logging.DEBUG, format='%(processName)s PID %(process)d: %(threadName)s:  %(message)s',)
from collections import namedtuple
import re

"""
Compilador debug con logging
"""

tokens = [
    r'(?P<NUM>\d+)',
    r'(?P<PLUS>\+)',
    r'(?P<MINUS>-)',
    r'(?P<TIMES>\*)',
    r'(?P<DIVIDE>/)',
    r'(?P<WS>\s+)',
    ]


master_re = re.compile('|'.join(tokens))
logging.info(f'master_re: {master_re}')
Token = namedtuple('Token', ['type','value'])
logging.info(f'Token: {Token}')

def tokenize(text):
    logging.info(f"tokenize text: {text} seguimos con el generador de tokens")
    return (Token(m.lastgroup, m.group()) for m in master_re.finditer(text) if m.lastgroup != 'WS')    
"""
La clase Node crea atributos a las clases BinOp y Number cuyo valor son los args pasados
"""
class Node:
    logging.info(f"Node")
    _fields = []
    logging.info(f"Node _fields:{_fields}")
    def __init__(self, *args):
        logging.info(f"Node init self: {self} args:{args}")
        for name, value in zip(self._fields, args):
            logging.info(f"Node for init self._fields: {self._fields} args: {args} name:{name} value:{value}")
            setattr(self, name, value)
            logging.info(f"Node for self:{self} name:{name} value: {value} self.__dict:{self.__dict__}")
"""
en BinOp se crea el campo _fields como una lista, cada item de esta lista es tomado
por la clase Node como insumo y es creado un objeto tipo BinOp con atributos asi:
objectBigOp=BigOp (op="+")
objectBigOp=BigOp (left="NumberObject")
"""           
class BinOp(Node):
    logging.info(f"BinOp")
    _fields = ['op', 'left', 'right']
    logging.info(f"BinOp _fields:{_fields}")

"""
Number hace lo mismo que BinOp pero en el campo _fields
solo se guardan Numeros
objectNumber= Number(value=2)
"""
class Number(Node):
    logging.info(f"Number")
    _fields = ['value']
    logging.info(f"Number _field : {_fields}")
"""
nonlocal: se usa cundo hay una variable en funciones anidadas
lo que hace es que los cambia que se efectúen es esta variable en las funciones
internas, cambian el valor de la externa. es decir si lookahead y current cambian en accept,
también cambian en parse.
"""

def parse(toks):
    logging.info(f"parse toks:{toks}")
    lookahead, current = next(toks, None), None
    logging.info(f"parse lookahead:{lookahead} current:{current}")

    def accept(*toktypes):
        logging.info(f"parse accept toktypes:{toktypes}")
        nonlocal lookahead, current
        logging.info(f"parse accept lookahead:{lookahead} current:{current} toktypes:{toktypes}")
        logging.info(f"parse accept  sigue if lookahead and lookahead.type in toktypes:")
        if lookahead and lookahead.type in toktypes:
            logging.info(f"parse accept if lookahead:{lookahead} y lookahead.type:{lookahead.type} esta en toktypes:{toktypes}")
            current, lookahead = lookahead, next(toks, None)
            logging.info(f"parse accept if current:{current},lookahead:{lookahead} retornaremos true de donde fue llamado")
            return True

    def expr():
        logging.info(f"parse expr")
        left = term()
        logging.info(f"parse exp left:{left} sigue while accept('PLUS','MINUS')")
        while accept('PLUS','MINUS'):
        #logging.info(f"parse expr while sigue linea left = BinOp(current.value, left) current.value:{current.value} left:{left} left.value:{left.value}")
            left = BinOp(current.value, left)
            logging.info(f"parse expr while current.value:{current.value} left:{left}")
            left.right = term()
            logging.info(f"parse expr while left.right:{left.right} retornamos left:{left}")
        logging.info(f"parse expr se retornara left:{left}")
        return left

    def term():
        logging.info(f"parse term")
        left = factor()
        logging.info(f"parse term left:{left} sigue while accept('TIMES','DIVIDE')")
        while accept('TIMES','DIVIDE'):
            logging.info(f"parse term while current.value:{current.value} left:{left}")
            left = BinOp(current.value, left)
            logging.info(f"parse term while left:{left} ")
            left.right = factor()
            logging.info(f"parse term while left.right: {left.right} retornamos left:{left} left.dict:{left.__dict__} ")
        logging.info(f"parse term se retornara  a exp left:{left}")
        return left

    def factor():
        logging.info(f"parse factor sigue if accept('NUM')")
        if accept('NUM'):
            logging.info(f"parse factor if accept('NUM') sigue result= Number(int(current.value))")
            result= Number(int(current.value))
            logging.info(f'parse factor if result.value: {result.value} retornaremos a term el result: {result}  ')
            #result: <__main__.Number object at..
            return result
        else:
            raise SyntaxError()
    logging.info(f"parse retornaremos expr()")
    return expr()  

# ---------------Patron Visitor-------------------------------------------------


class NodeVisitor:
    logging.info(f"NodeVisitor")
    def visit(self, node):
        logging.info(f"NodeVisitor visit resolver getattr(self, 'visit_' + type(node).__name__)(node) llamado como result = Evaluator().visit(tree)")
        logging.info(f"NodeVisitor visit self:{self} node: {node} type(node): {type(node)} ")
        var1=type(node).__name__
        logging.info(f"NodeVisitor visit type(node).__name__:{var1} ")
        var11='visit_' + var1
        logging.info(f"NodeVisitor visit 'visit_' + type(node).__name__):{var11}")
        var2=getattr(self, var11)
        logging.info(f"NodeVisitor visit getattr(self, 'visit_' + type(node).__name__):{var2} sigue {var2}(node)")
        var3=var2(node)
        logging.info(f"NodeVisitor visit getattr(self, 'visit_' + type(node).__name__)(node):{var3}")
        #atributo=getattr(self, 'visit_' + type(node).__name__)(node)
        #logging.info(f"NodeVisitor visit atributo:{var3}")
        return var3

class Evaluator(NodeVisitor):
    logging.info(f"Evaluator")
    def visit_Number(self, node):
        logging.info(f"Evaluator visit_Number self:{self} node:{node} node.__dict__:{node.__dict__}")
        valor=node.value
        logging.info(f"Evaluator visit_Number node.value:{valor}")
        return valor

    def visit_BinOp(self, node):
        logging.info(f"Evaluator visit_BinOp self:{self} node:{node} node.__dict__:{node.__dict__}")
        logging.info(f"Evaluator visit_BinOp self.visit(node.left) node.left:{node.left} ")
        # la siguiente linea crea una recursion que no es Optima
        leftval = self.visit(node.left)
        logging.info(f"Evaluator visit_BinOp leftval:{leftval}")
        logging.info(f"Evaluator visit_BinOp  Sigue self.visit(node.right) node.right:{node.right} ")
        # la siguiente linea crea una recursion que no es Optima
        rightval = self.visit(node.right)
        logging.info(f"Evaluator visit_BinOp rightval:{rightval}")
        
        if node.op == '+':
            logging.info(f"Evaluator visit_BinOp  type(leftval):{type(leftval)} {leftval} {node.op} type(rightval):{type(rightval)} {rightval}")
            return leftval + rightval
        elif node.op == '-':
            logging.info(f"Evaluator visit_BinOp  type(leftval):{type(leftval)} {leftval} {node.op} type(rightval):{type(rightval)} {rightval}")
            return leftval - rightval
        elif node.op == '*':
            logging.info(f"Evaluator visit_BinOp  type(leftval):{type(leftval)} {leftval} {node.op} type(rightval):{type(rightval)} {rightval}")
            return leftval * rightval
        elif node.op == '/':
            logging.info(f"Evaluator visit_BinOp  type(leftval):{type(leftval)} {leftval} {node.op} type(rightval):{type(rightval)} {rightval}")
            return leftval * rightval

if __name__ == '__main__':
    text = '2+1*4-5*2'
    logging.info(f"text:{text}")
    toks = tokenize(text)
    logging.info(f'toks: {toks}')
    tree = parse(toks)  
    #tree: <__main__.BinOp object at 0x10097aa40>
    logging.info(f"tree: {tree}")
    logging.info('---- Evaluation')
    result = Evaluator().visit(tree)
    logging.info(f'Resultado: {result}')




