# encoding: utf-8
# module QuantConnect.Data.Custom.Tiingo calls itself Tiingo
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Tiingo(object):
    """ Helper class for Tiingo configuration """
    @staticmethod
    def SetAuthCode(authCode):
        """
        SetAuthCode(authCode: str)
            Sets the Tiingo API token.
        
            authCode: The Tiingo API token
        """
        pass

    AuthCode = ''
    IsAuthCodeSet = False
    __all__ = [
        'SetAuthCode',
    ]


class TiingoPrice(TradeBar, IBaseData, IBaseDataBar, IBar):
    """
    Tiingo daily price data
                https://api.tiingo.com/docs/tiingo/daily
    
    TiingoPrice()
    """
    def DataTimeZone(self):
        """
        DataTimeZone(self: TiingoPrice) -> DateTimeZone
        
            Specifies the data time zone for this data type. 
             This is useful for custom data types
        
            Returns: The NodaTime.DateTimeZone of this data type
        """
        pass

    def DefaultResolution(self):
        """
        DefaultResolution(self: TiingoPrice) -> Resolution
        
            Gets the default resolution for this data and 
             security type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: TiingoPrice, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Return the URL string source of the file. This 
             will be converted to a stream
        
        
            config: Configuration object
            date: Date of this source file
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: String URL of source file.
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: TiingoPrice, config: SubscriptionDataConfig, content: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reader converts each line of the data source into 
             BaseData objects. Each data type creates its own 
             factory method,
                        and returns a 
             new instance of the object
                        each 
             time it is called. The returned object is assumed 
             to be time stamped in the 
             config.ExchangeTimeZone.
        
        
            config: Subscription data config setup object
            content: Content of the source document
            date: Date of the requested data
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: Instance of the T:BaseData object generated by 
             this line of the CSV
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: TiingoPrice) -> bool
        
            Indicates if there is support for mapping
            Returns: True indicates mapping should be used
        """
        pass

    def SupportedResolutions(self):
        """
        SupportedResolutions(self: TiingoPrice) -> List[Resolution]
        
            Gets the supported resolution for this data and 
             security type
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AdjustedClose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The adjusted close price of the asset on the specific date. Returns null if not available.

Get: AdjustedClose(self: TiingoPrice) -> Decimal

Set: AdjustedClose(self: TiingoPrice) = value
"""

    AdjustedHigh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The adjusted high price of the asset on the specific date. Returns null if not available.

Get: AdjustedHigh(self: TiingoPrice) -> Decimal

Set: AdjustedHigh(self: TiingoPrice) = value
"""

    AdjustedLow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The adjusted low price of the asset on the specific date. Returns null if not available.

Get: AdjustedLow(self: TiingoPrice) -> Decimal

Set: AdjustedLow(self: TiingoPrice) = value
"""

    AdjustedOpen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The adjusted opening price of the asset on the specific date. Returns null if not available.

Get: AdjustedOpen(self: TiingoPrice) -> Decimal

Set: AdjustedOpen(self: TiingoPrice) = value
"""

    AdjustedVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The adjusted number of shares traded during the day - adjusted for splits. Returns null if not available

Get: AdjustedVolume(self: TiingoPrice) -> Int64

Set: AdjustedVolume(self: TiingoPrice) = value
"""

    Close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual (not adjusted) closing price of the asset on the specific date

Get: Close(self: TiingoPrice) -> Decimal

Set: Close(self: TiingoPrice) = value
"""

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date this data pertains to

Get: Date(self: TiingoPrice) -> DateTime

Set: Date(self: TiingoPrice) = value
"""

    Dividend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The dividend paid out on "date" (note that "date" will be the "exDate" for the dividend)

Get: Dividend(self: TiingoPrice) -> Decimal

Set: Dividend(self: TiingoPrice) = value
"""

    EndTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The end time of this data. Some data covers spans (trade bars) and as such we want
            to know the entire time span covered

Get: EndTime(self: TiingoPrice) -> DateTime

Set: EndTime(self: TiingoPrice) = value
"""

    High = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual (not adjusted) high price of the asset on the specific date

Get: High(self: TiingoPrice) -> Decimal

Set: High(self: TiingoPrice) = value
"""

    Low = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual (not adjusted) low price of the asset on the specific date

Get: Low(self: TiingoPrice) -> Decimal

Set: Low(self: TiingoPrice) = value
"""

    Open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual (not adjusted) open price of the asset on the specific date

Get: Open(self: TiingoPrice) -> Decimal

Set: Open(self: TiingoPrice) = value
"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The period of this trade bar, (second, minute, daily, ect...)

Get: Period(self: TiingoPrice) -> TimeSpan

"""

    SplitFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A factor used when a company splits or reverse splits. On days where there is ONLY a split (no dividend payment),
            you can calculate the adjusted close as follows: adjClose = "Previous Close"/splitFactor

Get: SplitFactor(self: TiingoPrice) -> Decimal

Set: SplitFactor(self: TiingoPrice) = value
"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual (not adjusted) number of shares traded during the day

Get: Volume(self: TiingoPrice) -> Decimal

Set: Volume(self: TiingoPrice) = value
"""



class TiingoDailyData(TiingoPrice, IBaseData, IBaseDataBar, IBar):
    """
    Tiingo daily price data
                https://api.tiingo.com/docs/tiingo/daily
    
    TiingoDailyData()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class TiingoNews(IndexedBaseData, IBaseData):
    """
    Tiingo news data
                https://api.tiingo.com/documentation/news
    
    TiingoNews()
    """
    def DataTimeZone(self):
        """
        DataTimeZone(self: TiingoNews) -> DateTimeZone
        
            Specifies the data time zone for this data type. 
             This is useful for custom data types
        
            Returns: The NodaTime.DateTimeZone of this data type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: TiingoNews, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            For backtesting returns the index source for a 
             date
                    For live trading will return 
             the source url to use, not using the index 
             mechanism
        
        
            config: Configuration object
            date: Date of this source file
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: The QuantConnect.Data.SubscriptionDataSource 
             instance to use
        """
        pass

    def GetSourceForAnIndex(self, config, date, index, isLiveMode):
        """
        GetSourceForAnIndex(self: TiingoNews, config: SubscriptionDataConfig, date: DateTime, index: str, isLiveMode: bool) -> SubscriptionDataSource
        
            Returns the source for a given index value
        
            config: Configuration object
            date: Date of this source file
            index: The index value for which we want to fetch the 
             source
        
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: The QuantConnect.Data.SubscriptionDataSource 
             instance to use
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: TiingoNews, config: SubscriptionDataConfig, content: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reader converts each line of the data source into 
             BaseData objects. Each data type creates its own 
             factory method,
                        and returns a 
             new instance of the object
                        each 
             time it is called. The returned object is assumed 
             to be time stamped in the 
             config.ExchangeTimeZone.
        
        
            config: Subscription data config setup object
            content: Content of the source document
            date: Date of the requested data
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: Instance of the T:BaseData object generated by 
             this line of the CSV
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: TiingoNews) -> bool
        
            Indicates if there is support for mapping
            Returns: True indicates mapping should be used
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ArticleID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unique identifier specific to the news article.

Get: ArticleID(self: TiingoNews) -> str

Set: ArticleID(self: TiingoNews) = value
"""

    CrawlDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The datetime the news story was added to Tiingos database in UTC.
            This is always recorded by Tiingo and the news source has no input on this date.

Get: CrawlDate(self: TiingoNews) -> DateTime

Set: CrawlDate(self: TiingoNews) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Long-form description of the news story.

Get: Description(self: TiingoNews) -> str

Set: Description(self: TiingoNews) = value
"""

    PublishedDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The datetime the news story was published in UTC. This is usually reported by the news source and not by Tiingo.
            If the news source does not declare a published date, Tiingo will use the time the news story was discovered by our crawler farm.

Get: PublishedDate(self: TiingoNews) -> DateTime

Set: PublishedDate(self: TiingoNews) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The domain the news source is from.

Get: Source(self: TiingoNews) -> str

Set: Source(self: TiingoNews) = value
"""

    Symbols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """What symbols are mentioned in the news story.

Get: Symbols(self: TiingoNews) -> List[Symbol]

Set: Symbols(self: TiingoNews) = value
"""

    Tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tags that are mapped and discovered by Tiingo.

Get: Tags(self: TiingoNews) -> List[str]

Set: Tags(self: TiingoNews) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Title of the news article.

Get: Title(self: TiingoNews) -> str

Set: Title(self: TiingoNews) = value
"""

    Url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """URL of the news article.

Get: Url(self: TiingoNews) -> str

Set: Url(self: TiingoNews) = value
"""



class TiingoNewsJsonConverter(JsonConverter):
    """
    Helper json converter class used to convert a list of Tiingo news data
                into System.Collections.Generic.List
    
    TiingoNewsJsonConverter(symbol: Symbol)
    """
    def CanConvert(self, objectType):
        """
        CanConvert(self: TiingoNewsJsonConverter, objectType: Type) -> bool
        
            Determines whether this instance can convert the 
             specified object type.
        
        
            objectType: Type of the object.
            Returns: true if this instance can convert the specified 
             object type; otherwise, false.
        """
        pass

    @staticmethod
    def DeserializeNews(token):
        """
        DeserializeNews(token: JToken) -> TiingoNews
        
            Helper method to deserialize a single json Tiingo 
             news
        
        
            token: The json token containing the Tiingo news to 
             deserialize
        
            Returns: The deserialized 
             QuantConnect.Data.Custom.Tiingo.TiingoNews 
             instance
        """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """
        ReadJson(self: TiingoNewsJsonConverter, reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object
        
            Reads the JSON representation of the object.
        
            reader: The Newtonsoft.Json.JsonReader to read from.
            objectType: Type of the object.
            existingValue: The existing value of object being read.
            serializer: The calling serializer.
            Returns: The object value.
        """
        pass

    def WriteJson(self, writer, value, serializer):
        """
        WriteJson(self: TiingoNewsJsonConverter, writer: JsonWriter, value: object, serializer: JsonSerializer)
            Writes the JSON representation of the object.
        
            writer: The Newtonsoft.Json.JsonWriter to write to.
            value: The value.
            serializer: The calling serializer.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol):
        """ __new__(cls: type, symbol: Symbol) """
        pass


class TiingoSymbolMapper(object):
    """ Helper class to map a Lean format ticker to Tiingo format """
    @staticmethod
    def GetLeanTicker(ticker):
        """
        GetLeanTicker(ticker: str) -> str
        
            Maps a given Tiingo ticker to Lean equivalent
        """
        pass

    @staticmethod
    def GetTiingoTicker(symbol):
        """
        GetTiingoTicker(symbol: Symbol) -> str
        
            Maps a given QuantConnect.Symbol instance to it's 
             Tiingo equivalent
        """
        pass

    __all__ = [
        'GetLeanTicker',
        'GetTiingoTicker',
    ]


