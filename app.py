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
        for k in range( 0, len(X) + 1 - 3 ):
            for i in range( 0, len( X[0] ) + 1 - 3 ): 
                x = X[ k:k + 3, i:( i + 3 ) ]
                y = ( x * self.weights ).sum()
                conv1[k][i] = y
#        return conv1
        print( conv1 )
    
    def __call__( self, X ):
        return self.forward( X )



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

conv1 = np.random.randn( 6, 7 )

neuron(X)
