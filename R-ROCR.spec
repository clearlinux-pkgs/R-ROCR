#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ROCR
Version  : 1.0.11
Release  : 34
URL      : https://cran.r-project.org/src/contrib/ROCR_1.0-11.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ROCR_1.0-11.tar.gz
Summary  : Visualizing the Performance of Scoring Classifiers
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-gplots
BuildRequires : R-gplots
BuildRequires : buildreq-R

%description
and precision/recall plots are popular examples of trade-off
  visualizations for specific pairs of performance measures. ROCR is a
  flexible tool for creating cutoff-parameterized 2D performance curves
  by freely combining two from over 25 performance measures (new
  performance measures can be added using a standard interface).
  Curves from different cross-validation or bootstrapping runs can be
  averaged by different methods, and standard deviations, standard
  errors or box plots can be used to visualize the variability across
  the runs. The parameterization can be visualized by printing cutoff
  values at the corresponding curve positions, or by coloring the
  curve according to cutoff. All components of a performance plot can
  be quickly adjusted using a flexible parameter dispatching
  mechanism. Despite its flexibility, ROCR is easy to use, with only
  three commands and reasonable default values for all optional
  parameters.

%prep
%setup -q -c -n ROCR
cd %{_builddir}/ROCR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589750874

%install
export SOURCE_DATE_EPOCH=1589750874
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ROCR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ROCR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ROCR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ROCR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ROCR/CITATION
/usr/lib64/R/library/ROCR/DESCRIPTION
/usr/lib64/R/library/ROCR/INDEX
/usr/lib64/R/library/ROCR/Meta/Rd.rds
/usr/lib64/R/library/ROCR/Meta/data.rds
/usr/lib64/R/library/ROCR/Meta/demo.rds
/usr/lib64/R/library/ROCR/Meta/features.rds
/usr/lib64/R/library/ROCR/Meta/hsearch.rds
/usr/lib64/R/library/ROCR/Meta/links.rds
/usr/lib64/R/library/ROCR/Meta/nsInfo.rds
/usr/lib64/R/library/ROCR/Meta/package.rds
/usr/lib64/R/library/ROCR/Meta/vignette.rds
/usr/lib64/R/library/ROCR/NAMESPACE
/usr/lib64/R/library/ROCR/NEWS
/usr/lib64/R/library/ROCR/R/ROCR
/usr/lib64/R/library/ROCR/R/ROCR.rdb
/usr/lib64/R/library/ROCR/R/ROCR.rdx
/usr/lib64/R/library/ROCR/data/ROCR.hiv.rda
/usr/lib64/R/library/ROCR/data/ROCR.simple.rda
/usr/lib64/R/library/ROCR/data/ROCR.xval.rda
/usr/lib64/R/library/ROCR/demo/ROCR.R
/usr/lib64/R/library/ROCR/doc/ROCR.R
/usr/lib64/R/library/ROCR/doc/ROCR.Rmd
/usr/lib64/R/library/ROCR/doc/ROCR.html
/usr/lib64/R/library/ROCR/doc/index.html
/usr/lib64/R/library/ROCR/help/AnIndex
/usr/lib64/R/library/ROCR/help/ROCR.rdb
/usr/lib64/R/library/ROCR/help/ROCR.rdx
/usr/lib64/R/library/ROCR/help/aliases.rds
/usr/lib64/R/library/ROCR/help/paths.rds
/usr/lib64/R/library/ROCR/html/00Index.html
/usr/lib64/R/library/ROCR/html/R.css
/usr/lib64/R/library/ROCR/tests/testthat.R
/usr/lib64/R/library/ROCR/tests/testthat/test-aux.r
/usr/lib64/R/library/ROCR/tests/testthat/test-consistency.r
/usr/lib64/R/library/ROCR/tests/testthat/test-plot.r
/usr/lib64/R/library/ROCR/tests/testthat/test-simple.r
