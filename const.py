class ConstException(RuntimeError):
    pass

import copy
class const:
    def __init__(self, obj):
        self.__obj = obj
    def to_nonconst(self):
        return copy.deepcopy(self.__obj)
    def __val(self, item):
        if isinstance(item,const):
            return item.__obj
        else:
            return item
    def __del__(self):
        del self.__obj
    def __repr__(self):
        return repr(self.__obj)
    def __str__(self):
        return str(self.__obj)
    def __lt__(self, other):
        return self.__obj < self.__val(other)
    def __le__(self, other):
        return self.__obj <= self.__val(other)
    def __eq__(self, other):
        return self.__obj == self.__val(other)
    def __ne__(self, other):
        return self.__obj != self.__val(other)
    def __gt__(self, other):
        return self.__obj > self.__val(other)
    def __ge__(self, other):
        return self.__obj >= self.__val(other)
    # no need for __cmp__ since we have all rich comparisons
    def __hash__(self):
        return hash(self.__obj)
    def __nonzero__(self):
        return bool(self.__obj)
    def __unicode__(self):
        return unicode(self.__obj)
    def __getattr__(self, name):
        if name == '_const__obj':
            return self.__dict__[name]
        else:
            return const(getattr(self.__obj,name))
    def __setattr__(self, name, value):
        if name == '_const__obj':
            self.__dict__[name] = value
        else:
            raise ConstException('trying to change a constants attributes')
    def __delattr__(self, name):
        if name != '_const__obj':
            raise ConstException('trying to delete a constants attributes')
    # __getattribute__, __get__, __set__, __delete__, __slots__
    def __call__(self, *args, **kwds):
        return self.__obj(*args, **kwds)
    def __len__(self):
        return len(self.__obj)
    def __getitem__(self, key):
        return const(self.__obj[key])
    def __setitem__(self, key, value):
        raise ConstException('trying to change a constants items')
    def __delitem__(self, key, value):
        raise ConstException('trying to delete a constants items')
    def __iter__(self):
        return iter(self.__obj) #TODO need to make sure items iterated over aren't changed
    def __reversed__(self):
        return reversed(self.__obj)
    def __contains__(self, item):
        return item in self.__obj
    def __getslice__(self, i, j):
        return const(self.__obj[i:j])
    def __setslice__(self, i, j, sequence):
        raise ConstException('trying to change a constants items')
    def __delslice__(self, i, j):
        raise ConstException('trying to delete a constants items')
    def __add__(self, other):
        return self.__obj + self.__val(other)
    def __sub__(self, other):
        return self.__obj - self.__val(other)
    def __mul__(self, other):
        return self.__obj * self.__val(other)
    def __floordiv__(self, other):
        return self.__obj // self.__val(other)
    def __mod__(self, other):
        return self.__obj % self.__val(other)
    def __divmod__(self, other):
        return divmod(self.__obj, self.__val(other))
    def __pow__(self, other, module=None):
        return pow(self.__obj, self.__val(other),modulo)
    def __lshift__(self, other):
        return self.__obj << self.__val(other)
    def __rshift__(self, other):
        return self.__obj >> self.__val(other)
    def __and__(self, other):
        return self.__obj & self.__val(other)
    def __xor__(self, other):
        return self.__obj ^ self.__val(other)
    def __or__(self, other):
        return self.__obj | self.__val(other)
    def __div__(self, other):
        return self.__obj / self.__val(other)
    def __truediv__(self, other):
        return self.__obj / self.__val(other)
    def __radd__(self, other):
        return  self.__val(other) + self.__obj
    def __rsub__(self, other):
        return  self.__val(other) - self.__obj
    def __rmul__(self, other):
        return  self.__val(other) * self.__obj
    def __rdiv__(self, other):
        return  self.__val(other) / self.__obj
    def __rtruediv__(self, other):
        return  self.__val(other) / self.__obj
    def __rfloordiv__(self, other):
        return  self.__val(other) // self.__obj
    def __rmod__(self, other):
        return  self.__val(other) % self.__obj
    def __rdivmod__(self, other):
        return divmod(self.__val(other), self.__obj)
    def __rpow__(self, other):
        return pow(self.__val(other), self.__obj)
    def __rlshift__(self, other):
        return  self.__val(other) << self.__obj
    def __rrshift__(self, other):
        return  self.__val(other) >> self.__obj
    def __rand__(self, other):
        return  self.__val(other) & self.__obj
    def __rxor__(self, other):
        return  self.__val(other) ^ self.__obj
    def __ror__(self, other):
        return  self.__val(other) | self.__obj
    def __iadd__(self, other):
        raise ConstException('trying to change a constants value')
    def __isub__(self, other):
        raise ConstException('trying to change a constants value')
    def __imul__(self, other):
        raise ConstException('trying to change a constants value')
    def __idiv__(self, other):
        raise ConstException('trying to change a constants value')
    def __itruediv__(self, other):
        raise ConstException('trying to change a constants value')
    def __ifloordiv__(self, other):
        raise ConstException('trying to change a constants value')
    def __imod__(self, other):
        raise ConstException('trying to change a constants value')
    def __ipow__(self, other):
        raise ConstException('trying to change a constants value')
    def __ilshift__(self, other):
        raise ConstException('trying to change a constants value')
    def __irshift__(self, other):
        raise ConstException('trying to change a constants value')
    def __iand__(self, other):
        raise ConstException('trying to change a constants value')
    def __ixor__(self, other):
        raise ConstException('trying to change a constants value')
    def __ior__(self, other):
        raise ConstException('trying to change a constants value')
    def __neg__(self):
        return -self.__obj
    def __pos__(self):
        return +self.__obj
    def __abs__(self):
        return abs(self.__obj)
    def __invert__(self):
        return ~self.__obj
    def __complex__(self):
        return complex(self.__obj)
    def __int__(self):
        return int(self.__obj)
    def __long__(self):
        return long(self.__obj)
    def __float__(self):
        return float(self.__obj)
    def __oct__(self):
        return oct(self.__obj)
    def __hex__(self):
        return hex(self.__obj)
    def __index__(self):
        return operator.index(self.__obj)
    def __coerce__(self, other):
        if isinstance(other, const):
            return self, other
        else:
            return self, const(other)


import sys
def tracefunc(frame, event, arg):
    local_adds = []
    for name in frame.f_locals:
        prefix = '___local_const_type___'
        if isinstance(frame.f_locals[name], const) and not name.startswith(prefix):
            local_adds.append(('%s%s'%(prefix,name), frame.f_locals[name]))
        elif name.startswith(prefix) and (name[len(prefix):] not in frame.f_locals or id(frame.f_locals[name[len(prefix):]]) != id(frame.f_locals[name])):
            raise ConstException('constant %s changed!'%name[len(prefix):])
    for name,value in local_adds:
        frame.f_locals[name] = value
    return tracefunc

def test_one(i):
    global t
    t = const('global constant')
    z = i.to_nonconst()
    z = 9
    x = const(5)
    t = 'yup' #TODO add f_globals too
    print(t)
    print(i)
    z = const(9)
    print(x)
    print(z+x)
    z = 3
#    return x

def test():
#    for i in xrange(100000):
#        x=i
#    return
    p = const('hello')
    y = test_one(p)
    #p += 'ahh'
    y = 4
    print(p)

import time
if __name__ == '__main__':
#    start = time.time()
#    for i in xrange(100000):
#        x=i
#    print('first',time.time()-start)
    sys.settrace(tracefunc)
#    start = time.time()
    test()
#    print('withtrace',time.time()-start)

