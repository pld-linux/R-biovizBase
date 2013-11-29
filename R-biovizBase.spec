%define		packname	biovizBase

Summary:	Basic graphic utilities for visualization of genomic data
Name:		R-%{packname}
Version:	1.10.4
Release:	1
License:	Artistic 2.0
Group:		X11/Applications
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	c9f2652887977e5283bcbb6b9e30b14a
URL:		http://www.bioconductor.org/packages/release/bioc/html/biovizBase.html
BuildRequires:	R
BuildRequires:	R-cran-scales
BuildRequires:	R-cran-Hmisc
BuildRequires:	R-cran-RColorBrewer
BuildRequires:	R-cran-dichromat
BuildRequires:	R-GenomicRanges
BuildRequires:	R-Biostrings
BuildRequires:	R-Rsamtools
BuildRequires:	R-GenomicFeatures
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-scales
Requires:	R-Hmisc
Requires:	R-RColorBrewer
Requires:	R-dichromat
Requires:	R-GenomicRanges
Requires:	R-Biostrings
Requires:	R-Rsamtools
Requires:	R-GenomicFeatures
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The biovizBase package is designed to provide a set of utilities,
color schemes and conventions for genomic data. It serves as the base
for various high-level packages for biological data visualization.
This saves development effort and encourages consistency.

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc/
%doc %{_libdir}/R/library/%{packname}/html/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/data/
%{_libdir}/R/library/%{packname}/examples/
%{_libdir}/R/library/%{packname}/extdata/
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/biovizBase.so
