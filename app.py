#!/usr/bin/env python3

print( "Hi" )


class ConvolutionNeuron:
    
    def __init__( self ):
        self.weight = [[[ 0, 1, 0 ],
                        [ 0, 1, 0 ],
                        [ 0, 1, 0 ]
                    ]]

    def forward( self, X ):
        return X * self.weight + self.bias

    def __call__( self, X ):
        return self.forward( X )


neuron = LinearNeuron()

neuron.weight = 1
neuron.bias   = 1

X = [ 1, 44, 45, 46, 47, 2, 3, 4, 5, 6, 0, -1, -2, -3, -4 ]
Y = []

for x in X:
    y = neuron( x )
    Y.append( y )

print( X )
print( Y )

