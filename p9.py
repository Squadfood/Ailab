import pandas as pd 
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
data=pd.read_csv('heart1.csv')
model=BayesianNetwork([('age', 'heartdisease'),
                        ('gender', 'heartdisease'),
                        ('family', 'heartdisease'),
                        ('diet', 'heartdisease'),
                        ('lifestyle', 'heartdisease'),
                        ('cholestrol', 'heartdisease')])
model.fit(data,estimator=MaximumLikelihoodEstimator)
infer=VariableElimination(model)
q1=infer.query(variables=['heartdisease'],evidence={'diet': 1})
print(q1)
q2 = infer.query(variables=['heartdisease'], evidence={'lifestyle': 2})
print(q2)

