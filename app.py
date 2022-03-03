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


weights = np.array ([
                     [ 0, 1, 0 ],
                     [ 0, 1, 0 ],
                     [ 0, 1, 0 ]
                   ])
#neuron = ConvolutionNeuron()
conv1 = np.random.randn( 6, 7 )

#print( f"\narray X >>>\n{X}" )
#print( f"X shape >>> {X.shape}" ) 
#print( f"len axis string >>> {len( X )}" )
#print( f"len axis column >>> {len( X[0] )}" )
#print( f"\nweights >>>\n{weights}")



for i in range( 0, len( X[0] ) + 1 - 3 ): 
    x = X[ 0:3, i:( i + 3 ) ]
    print( f"\nx({i}) >>> \n{x}" )
    y = ( x * weights ).sum()
    conv1[0][i] = y


print( conv1 )



