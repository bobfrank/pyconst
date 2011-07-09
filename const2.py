#   this is probably the second fastest and most powerful since once
# this works right type checking could also potentially be added

import dis
import parser
import opcode

const = lambda x:x

def misc(num,second=4):
    return const(num+second)

def fun():
    x = misc(const(4))
    print type(dis.dis)
    y = 4
    x = const(misc(1,6))
    return x

print fun()

class norebind:
    pass

def disassemble(co):
    code = co.co_code
    print co.co_consts
    print co.co_names
    print co.co_argcount, co.co_varnames
    byte_increments = [ord(c) for c in co.co_lnotab[0::2]]
    line_increments = [ord(c) for c in co.co_lnotab[1::2]]
    deltas = zip(byte_increments, line_increments)
    if len(deltas) > 0:
        lasti = deltas.pop()
    else:
        lasti = (1000000,1000000)
    istart = 0
    line = co.co_firstlineno+1
    n = len(code)
    i = 0
    extended_arg = 0

    free = None
    while i < n:
        if i-istart >= lasti[0]:
            line += lasti[1]
            if len(deltas) > 0:
                lasti = deltas.pop()
            else:
                lasti = (1000000,1000000)
            istart = i
        c = code[i]
        op = ord(c)
        #print co.co_filename, line,i-istart,lasti
        print repr(i).rjust(4),
        print opcode.opname[op].ljust(20),
        i = i+1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = ord(code[i]) + ord(code[i+1])*256 + extended_arg
            extended_arg = 0
            i = i+2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg*65536L
            print repr(oparg).rjust(5),
            if op in opcode.hasconst:
                print 'c(' + repr(co.co_consts[oparg]) + ')',
            elif op in opcode.hasname:
                print 'n(' + co.co_names[oparg] + ')',
            elif op in opcode.hasjrel:
                print 'j(to ' + repr(i + oparg) + ')',
            elif op in opcode.haslocal:
                print 'l(' + co.co_varnames[oparg] + ')',
            elif op in opcode.hascompare:
                print 'cmp(' + opcode.cmp_op[oparg] + ')',
            elif op in opcode.hasfree:
                if free is None:
                    free = co.co_cellvars + co.co_freevars
                print 'f(' + free[oparg] + ')',
        print
disassemble(fun.func_code)


def validate_method(item,nstack):
    if not hasattr(item, 'func_code'):
        #TODO give a warning
        return
    else:
        print '.'.join(nstack),'()'
        disassemble(item.func_code)

import inspect
def validate_module(mod, nstack):
    for name in dir(mod):
        item = getattr(mod,name)
        if inspect.isclass(item) and name != '__class__':
            validate_module(item,nstack+[name])
        elif inspect.ismethod(item):
            validate_method(item,nstack+[name])

import __builtin__
x = __builtin__.__import__
def mine(name,*args,**kwds):
   out = x(name,*args,**kwds)
   validate_module(out, [name])
   return out
__builtin__.__import__ = mine

import boto
