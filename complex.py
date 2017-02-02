class Complex(object):
  def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary

  def toString(self):
    return str(self.real) + " + "  + str(self.imaginary) + "i"

  def add(self, other):
    return Complex(self.real + other.real, self.imaginary + other.imaginary)

a = Complex(1, 2)
b = Complex(3, 4)
c = a.add(b)

print "A %s" % a.toString()
print "B %s" % b.toString()
print "C %s" % c.toString()
