close all
clear all
clc

name = 'matrix.mtx';
A = mmread(name);

A_dof = size(A, 1);
['dof ' num2str(A_dof)]

A_nnz = nnz(A);
['nnz ' num2str(A_nnz)]

A_sparsity = A_nnz/A_dof^2;
['nnz/dof^2 ' num2str(A_sparsity)]

A_cond = condest(A);
['cond2 ' num2str(A_cond)]
