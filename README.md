# Verification and validation repository for QGD/Hybrid solvers

The primary objective of the repository to gather and keep updated verification and validation problems showing strengths and weakneses of the aforementioned computational complexes.

## Available cases

Next cases are available (uploaded to the repository):

- [the Sod's shock tube](https://github.com/mkraposhin/VnV/tree/main/SodProblem);
- [the 2 rarefaction proble](https://github.com/mkraposhin/VnV/tree/main/TwoRarefactionWaves);
- [the two shocks problem](https://github.com/mkraposhin/VnV/tree/main/TwoShocks);
- [the two gases diffusion case](https://github.com/mkraposhin/VnV/tree/main/GasesDiffusion);
- [the forward step](https://github.com/mkraposhin/VnV/tree/main/ForwardStep);
- [the Sod's problem for two gases](https://github.com/mkraposhin/VnV/tree/main/TwoGasesSodProblem);
- [a 1D reactive tube](https://github.com/mkraposhin/VnV/tree/main/Reactive1dTube);
- [Re=100 bakward facing step](https://github.com/mkraposhin/VnV/tree/main/BackwardStepIco);
- [a planar acoustic wave propagation](https://github.com/mkraposhin/VnV/tree/main/PlanarAcousticWave);
- [a converging-diverging nozzle](https://github.com/mkraposhin/VnV/tree/main/ConverginDivergingNozzle).

## Cases with automatied verification procedure

- [the Sod's shock tube](https://github.com/mkraposhin/VnV/tree/main/SodProblem)

## The structure of the repository

The structure of the repository is next.

1. On the first level go folders with titles of problems.
2. On the second level inside a problem folder we keep folders:
   - for reference data (reference/);
   - for literature (docs/);
   - for results of comparison (comparison/) with reference data and between different solvers;
   - for cases computed using different solvers (e.g., QGDFoam/, pimpleCentralFoam/, rhoCentralFoam/, etc);
   - for common data shared by different solvers (common/) cases.
3. On the third level, inside the solver folders we keep computational cases in folders with names specifying the mesh density (e.g., 10CPL, 20CPL, etc).

The wish list of cases to check is maintained using the [issues](https://github.com/mkraposhin/VnV/issues) section of the repository with all neccesary links to reference data and description of problems.  

## Examples of the structure

    SodProblem/
        reference/
        docs/
        comparison/
        QGDFoam/
            100CPL/
            200CPL/
            400CPL/
        pimpleCentralFoam/
            100CPL/
            200CPL/
            400CPL/
    

