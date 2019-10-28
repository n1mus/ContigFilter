/*
A KBase module: suminwContigFilter
This sample module contains one small method that filters contigs.
*/

module suminwContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
	Example app that filters based on a minimum length
    */
    funcdef run_suminwContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;



    /*
	Example app that filters based on both a minimum and maximum length
    */
    funcdef run_suminwContigFilter_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;


};
