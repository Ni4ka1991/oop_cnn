#!/usr/bin/env python3
import numpy as np

class ConvolutionNeuron:
    
    def __init__( self ):
        self.weights = np.array([
                                 [ 0, 1, 0 ],
                                 [ 0, 1, 0 ],
                                 [ 0, 1, 0 ]
                               ])

    def forward( self, X ):
        return X * self.weight

    def __call__( self, X ):
        return self.forward( X )


Y = []

X = np.array ([
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

neuron = ConvolutionNeuron()
print( neuron.weights )
print( type( neuron.weights ))
print( f"weights dimension >>> {neuron.weights.ndim}")

print()
print( X )
print( X.ndim )















#for x in X:
#    y = neuron( x )
#    Y.append( y )

#print( X )
#print( Y )

