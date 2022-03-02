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

#X_tensor = X.flatten()

#neuron = ConvolutionNeuron()
#print( neuron.weights )
#print( type( neuron.weights ))
#print( f"weights dimension >>> {neuron.weights.ndim}")

print()
print( f"array X >>>\n{X}" )
#print( f"array X dimension >>> {X.ndim}" )
#print()
#print( f"array X_tensor >>>\n{X_tensor}" )
#print( f"array X_tensor dimension >>> {X_tensor.ndim}" )

weights = np.array ([
                     [ 0, 1, 0 ],
                     [ 0, 1, 0 ],
                     [ 0, 1, 0 ]
                   ])

#conv1 = np.random.randn( 6, 7 )   #7 colums 6 strings
#print( conv1 )
#print( conv1.ndim )

x_0 = X[:3]
print( f"x_0 >>>\n{x_0}" )
x_0_0 = x_0[ 0:3, 0:3 ]
print( f"\nx_0_0 >>>\n{x_0_0}" )

