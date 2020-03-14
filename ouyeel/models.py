from django.db import models

# Create your models here.


class Ouyeel(models.Model):

    bailScale = models.CharField(max_length=20, verbose_name="保证金比例", null=True, blank=True)
    balanceQuantity = models.CharField(max_length=20, verbose_name="数量", null=True, blank=True)
    balanceWeight = models.CharField(max_length=20, verbose_name="重量", null=True, blank=True)
    bargainDeduction = models.CharField(max_length=20, verbose_name="议价额度", null=True, blank=True)
    basicPrice = models.CharField(max_length=20, verbose_name="竞拍起始价格", null=True, blank=True)
    bastingWeight = models.CharField(max_length=20, verbose_name="假缝重量", null=True, blank=True)
    batchId = models.CharField(max_length=100, verbose_name="批次", null=True, blank=True)
    beCollected = models.CharField(max_length=20, verbose_name="已收集", null=True, blank=True)
    beReported = models.CharField(max_length=20, verbose_name="已报告", null=True, blank=True)
    beVisited = models.CharField(max_length=20, verbose_name="已访问", null=True, blank=True)
    bidBeginDate = models.CharField(max_length=20, verbose_name="出价起始时间", null=True, blank=True)
    bidEndDate = models.CharField(max_length=20, verbose_name="出价结束时间", null=True, blank=True)
    boundleId = models.CharField(max_length=20, verbose_name="困包标识", null=True, blank=True)
    businessTimes = models.CharField(max_length=20, verbose_name="竞价期间", null=True, blank=True)
    canCompensateFlag = models.CharField(max_length=20, verbose_name="可补偿", null=True, blank=True)
    coatingStructure = models.CharField(max_length=20, verbose_name="包装构成", null=True, blank=True)
    coatingType = models.CharField(max_length=100, verbose_name="包装类型", null=True, blank=True)
    color = models.CharField(max_length=20, verbose_name="颜色", null=True, blank=True)
    companyType = models.CharField(max_length=20, verbose_name="公司类型", null=True, blank=True)
    contactName = models.CharField(max_length=20, verbose_name="联系人", null=True, blank=True)
    contactPhone = models.CharField(max_length=20, verbose_name="联系电话", null=True, blank=True)
    contactQq = models.CharField(max_length=20, verbose_name="QQ", null=True, blank=True)
    createDate = models.CharField(max_length=20, verbose_name="上架时间", null=True, blank=True)
    depositAmt = models.CharField(max_length=20, verbose_name="定金额度", null=True, blank=True)
    displayZone = models.CharField(max_length=20, verbose_name="展示区域", null=True, blank=True)
    earnestRatio = models.CharField(max_length=20, verbose_name="定金比例", null=True, blank=True)
    factoryResCode = models.CharField(max_length=20, verbose_name="钢厂资源号", null=True, blank=True)
    firstPriceIncrement = models.CharField(max_length=20, verbose_name="首次价格增长", null=True, blank=True)
    gradenumThick = models.CharField(max_length=20, verbose_name="评级数量厚度", null=True, blank=True)
    hasBlockChainQualityCert = models.CharField(max_length=20, verbose_name="区块链质量认证", null=True, blank=True)
    hasFreight = models.CharField(max_length=20, verbose_name="运输服务", null=True, blank=True)
    hasFreightSubsidy = models.CharField(max_length=20, verbose_name="运输优惠", null=True, blank=True)
    hasQualityCert = models.CharField(max_length=20, verbose_name="质量证书", null=True, blank=True)
    hasQualityInfo = models.CharField(max_length=20, verbose_name="质量信息", null=True, blank=True)
    hasShop = models.CharField(max_length=20, verbose_name="竞拍是否开始", null=True, blank=True)
    hasVideo = models.CharField(max_length=20, verbose_name="有无视频", null=True, blank=True)
    isAddBid = models.CharField(max_length=20, verbose_name="有无竞价加价", null=True, blank=True)
    isAfterSettle = models.CharField(max_length=20, verbose_name="后续解决", null=True, blank=True)
    isAttention = models.CharField(max_length=20, verbose_name="是否关注", null=True, blank=True)
    isBailAllowed = models.CharField(max_length=20, verbose_name="允许担保", null=True, blank=True)
    isBargain = models.CharField(max_length=20, verbose_name="是否可议价", null=True, blank=True)
    isCompetitiveRes = models.CharField(max_length=20, verbose_name="任务开始时间", null=True, blank=True)
    isDelayAllowed = models.CharField(max_length=20, verbose_name="是否可延迟", null=True, blank=True)
    isFixed = models.CharField(max_length=20, verbose_name="是否固定", null=True, blank=True)
    isLoanAllowed = models.CharField(max_length=20, verbose_name="可否融资", null=True, blank=True)
    isLotteryTime = models.CharField(max_length=20, verbose_name="是否抽奖时间", null=True, blank=True)
    isMorgageAllowed = models.CharField(max_length=20, verbose_name="是否可抵质押", null=True, blank=True)
    isQuicklyWarehousing = models.CharField(max_length=20, verbose_name="短期周转性贷款", null=True, blank=True)
    isRolled = models.CharField(max_length=20, verbose_name="轧制的", null=True, blank=True)
    isTargeting = models.CharField(max_length=20, verbose_name="为目标标的物", null=True, blank=True)
    itemId = models.CharField(max_length=20, verbose_name="物品标识", null=True, blank=True)
    itemShape = models.CharField(max_length=20, verbose_name="物品形状", null=True, blank=True)
    latitude = models.CharField(max_length=20, verbose_name="经度", null=True, blank=True)
    location = models.CharField(max_length=20, verbose_name="坐落", null=True, blank=True)
    longitude = models.CharField(max_length=20, verbose_name="纬度", null=True, blank=True)
    manufactureCode = models.CharField(max_length=20, verbose_name="制造商编码", null=True, blank=True)
    manufactureDate = models.CharField(max_length=20, verbose_name="制造时间", null=True, blank=True)
    manufactureName = models.CharField(max_length=20, verbose_name="制造商名称", null=True, blank=True)
    maxDeduction = models.CharField(max_length=20, verbose_name="最大减除额", null=True, blank=True)
    maxPrice = models.CharField(max_length=20, verbose_name="最高价", null=True, blank=True)
    midTagPicUrl = models.CharField(max_length=100, verbose_name="标签图片地址", null=True, blank=True)
    minPrice = models.CharField(max_length=20, verbose_name="最低价", null=True, blank=True)
    minPublishTime = models.CharField(max_length=20, verbose_name="最早公开时间", null=True, blank=True)
    modiDate = models.CharField(max_length=20, verbose_name="修改时间", null=True, blank=True)
    modiPerson = models.CharField(max_length=20, verbose_name="修改人", null=True, blank=True)
    morgageOrgCode = models.CharField(max_length=20, verbose_name="抵押贷款组织编号", null=True, blank=True)
    morgageOrgName = models.CharField(max_length=20, verbose_name="任务开始组织名称", null=True, blank=True)
    morgageType = models.CharField(max_length=20, verbose_name="抵押贷款类型", null=True, blank=True)
    netWeight = models.CharField(max_length=20, verbose_name="网络重量", null=True, blank=True)
    newResource = models.CharField(max_length=20, verbose_name="新的资源", null=True, blank=True)
    onBusiness = models.CharField(max_length=20, verbose_name="是否正在交易", null=True, blank=True)
    ownerCode = models.CharField(max_length=20, verbose_name="所有者编号", null=True, blank=True)
    ownerName = models.CharField(max_length=20, verbose_name="所有人名称", null=True, blank=True)
    packCode = models.CharField(max_length=20, verbose_name="包装编号", primary_key=True)
    packType = models.CharField(max_length=20, verbose_name="包装类型", null=True, blank=True)
    paintType = models.CharField(max_length=20, verbose_name="涂印类型", null=True, blank=True)
    penaltyAmt = models.CharField(max_length=20, verbose_name="违约金额", null=True, blank=True)
    penaltyAmtRate = models.CharField(max_length=20, verbose_name="违约金比例", null=True, blank=True)
    pieces = models.CharField(max_length=20, verbose_name="分包数", null=True, blank=True)
    prodCat = models.CharField(max_length=20, verbose_name="产品猫", null=True, blank=True)
    productCode = models.CharField(max_length=20, verbose_name="产品编号", null=True, blank=True)
    productName = models.CharField(max_length=20, verbose_name="产品名称", null=True, blank=True)
    productTypeCode = models.CharField(max_length=20, verbose_name="产品类型编号", null=True, blank=True)
    productTypeName = models.CharField(max_length=20, verbose_name="产品类型名称", null=True, blank=True)
    promiseTime = models.CharField(max_length=20, verbose_name="承诺时间", null=True, blank=True)
    promotionIds = models.CharField(max_length=20, verbose_name="促销标识", null=True, blank=True)
    promotionTypes = models.CharField(max_length=20, verbose_name="促销类型", null=True, blank=True)
    providerCode = models.CharField(max_length=20, verbose_name="经销商编号", null=True, blank=True)
    providerCodeEncode = models.CharField(max_length=20, verbose_name="经销商编号编码(utf8)", null=True, blank=True)
    providerName = models.CharField(max_length=20, verbose_name="经销商名称", null=True, blank=True)
    providerPackCode = models.CharField(max_length=20, verbose_name="经销商包装编码", null=True, blank=True)
    providerProductCode = models.CharField(max_length=20, verbose_name="经销商产品编码", null=True, blank=True)
    providerProductName = models.CharField(max_length=20, verbose_name="经销商产品名称", null=True, blank=True)
    providerProductTypeCode = models.CharField(max_length=20, verbose_name="经销商产品类型编号", null=True, blank=True)
    providerProductTypeName = models.CharField(max_length=20, verbose_name="经销商产品类型名称", null=True, blank=True)
    providerResCode = models.CharField(max_length=20, verbose_name="经销应商结果编号", null=True, blank=True)
    providerShortName = models.CharField(max_length=20, verbose_name="经销商简称", null=True, blank=True)
    providerShowName = models.CharField(max_length=20, verbose_name="经销商字号", null=True, blank=True)
    publishDate = models.CharField(max_length=20, verbose_name="公开日期", null=True, blank=True)
    publishPrice = models.CharField(max_length=20, verbose_name="公开价格", null=True, blank=True)
    putinDate = models.CharField(max_length=20, verbose_name="入网时间", null=True, blank=True)
    qualityFlag = models.CharField(max_length=20, verbose_name="质量标准", null=True, blank=True)
    qualityGrade = models.CharField(max_length=20, verbose_name="质量等级", null=True, blank=True)
    qualityGradeName = models.CharField(max_length=100, verbose_name="质量等级名称", null=True, blank=True)
    quantity = models.CharField(max_length=20, verbose_name="数量", null=True, blank=True)
    quickInvoicingFlag = models.CharField(max_length=20, verbose_name="闪电开票", null=True, blank=True)
    realEndDate = models.CharField(max_length=20, verbose_name="实际结束日期", null=True, blank=True)
    realPictureStatus = models.CharField(max_length=20, verbose_name="真实图片状态", null=True, blank=True)
    recentBought = models.CharField(max_length=20, verbose_name="最近购买", null=True, blank=True)
    refShopSign = models.CharField(max_length=20, verbose_name="任务开始时间", null=True, blank=True)
    resFrom = models.CharField(max_length=20, verbose_name="结果来源", null=True, blank=True)
    resStatus = models.CharField(max_length=20, verbose_name="结果状态", null=True, blank=True)
    resourceId = models.CharField(max_length=20, verbose_name="资源标识", null=True, blank=True)
    resourceType = models.CharField(max_length=20, verbose_name="资源类型", null=True, blank=True)
    rzBankList = models.CharField(max_length=20, verbose_name="融资银行列表", null=True, blank=True)
    saleUserName = models.CharField(max_length=20, verbose_name="销售方用户名", null=True, blank=True)
    saleUserPhone = models.CharField(max_length=20, verbose_name="销售方手机号", null=True, blank=True)
    salesMethod = models.CharField(max_length=20, verbose_name="销售方法", null=True, blank=True)
    salesMode = models.CharField(max_length=20, verbose_name="销售模式", null=True, blank=True)
    sellerLevel = models.CharField(max_length=20, verbose_name="销售等级", null=True, blank=True)
    sellerMedal = models.CharField(max_length=20, verbose_name="销售者荣誉", null=True, blank=True)
    sellerScore = models.CharField(max_length=20, verbose_name="任务开始时间", null=True, blank=True)
    shopShortName = models.CharField(max_length=20, verbose_name="经销商简称", null=True, blank=True)
    shopSign = models.CharField(max_length=100, verbose_name="产品材质", null=True, blank=True)
    smallFrontPicUrl = models.CharField(max_length=150, verbose_name="前置图标url地址", null=True, blank=True)
    spec = models.CharField(max_length=20, verbose_name="规格", null=True, blank=True)
    spec1 = models.CharField(max_length=20, verbose_name="规格1", null=True, blank=True)
    spec2 = models.CharField(max_length=20, verbose_name="规格2", null=True, blank=True)
    spec3 = models.CharField(max_length=20, verbose_name="规格3", null=True, blank=True)
    spec4 = models.CharField(max_length=20, verbose_name="规格4", null=True, blank=True)
    spec5 = models.CharField(max_length=20, verbose_name="规格5", null=True, blank=True)
    spec6 = models.CharField(max_length=20, verbose_name="规格6", null=True, blank=True)
    specComment = models.CharField(max_length=255, verbose_name="规格简要说明", null=True, blank=True)
    specialComments = models.CharField(max_length=200, verbose_name="特别说明", null=True, blank=True)
    startingPrice = models.CharField(max_length=20, verbose_name="起始价格", null=True, blank=True)
    stdIncrement = models.CharField(max_length=20, verbose_name="标准加价", null=True, blank=True)
    stockFlag = models.CharField(max_length=20, verbose_name="库存标志", null=True, blank=True)
    storeCityCode = models.CharField(max_length=20, verbose_name="仓储城市编码", null=True, blank=True)
    storeCityName = models.CharField(max_length=20, verbose_name="仓储城市名称", null=True, blank=True)
    supervisionRate = models.CharField(max_length=20, verbose_name="监理等级", null=True, blank=True)
    surfaceDispose = models.CharField(max_length=20, verbose_name="表面处理", null=True, blank=True)
    surfaceProcess = models.CharField(max_length=100, verbose_name="表面处理过程工艺", null=True, blank=True)
    targetingCodes = models.CharField(max_length=20, verbose_name="目标编码", null=True, blank=True)
    techStandard = models.CharField(max_length=100, verbose_name="技术标准", null=True, blank=True)
    tensionKl = models.CharField(max_length=20, verbose_name="张力K1", null=True, blank=True)
    tensionQf = models.CharField(max_length=20, verbose_name="张力Qf", null=True, blank=True)
    tensionSc = models.CharField(max_length=20, verbose_name="张力Sc", null=True, blank=True)
    ticketRate = models.CharField(max_length=20, verbose_name="开票比率", null=True, blank=True)
    userCode = models.CharField(max_length=20, verbose_name="用户编码", null=True, blank=True)
    videoInspectionFlag = models.CharField(max_length=20, verbose_name="视频巡查（验货）", null=True, blank=True)
    warehouseCode = models.CharField(max_length=20, verbose_name="仓库编号", null=True, blank=True)
    warehouseName = models.CharField(max_length=20, verbose_name="仓库名称", null=True, blank=True)
    weekendBusiness = models.CharField(max_length=20, verbose_name="周末办公", null=True, blank=True)
    weight = models.CharField(max_length=20, verbose_name="重量", null=True, blank=True)
    weightMethod = models.CharField(max_length=20, verbose_name="计重方式", null=True, blank=True)
    whValidatedFlag = models.CharField(max_length=20, verbose_name="wh确认", null=True, blank=True)

    def __str__(self):
        return 'tinplate'

    def to_dic(self):
        goodsInfoes = {
            'bailScale': self.bailScale,
            'balanceQuantity': self.balanceQuantity,
            'balanceWeight': self.balanceWeight,
            'bargainDeduction': self.bargainDeduction,
            'basicPrice': self.basicPrice,
            'bastingWeight': self.bastingWeight,
            'batchId': self.batchId,
            'beCollected': self.beCollected,
            'beReported': self.beReported,
            'beVisited': self.beVisited,
            'bidBeginDate': self.bidBeginDate,
            'bidEndDate': self.bidEndDate,
            'boundleId': self.boundleId,
            'businessTimes': self.businessTimes,
            'canCompensateFlag': self.canCompensateFlag,
            'coatingStructure': self.coatingStructure,
            'coatingType': self.coatingType,
            'color': self.color,
            'companyType': self.companyType,
            'contactName': self.contactName,
            'contactPhone': self.contactPhone,
            'contactQq': self.contactQq,
            'createDate': self.createDate,
            'depositAmt': self.depositAmt,
            'displayZone': self.displayZone,
            'earnestRatio': self.earnestRatio,
            'factoryResCode': self.factoryResCode,
            'firstPriceIncrement': self.firstPriceIncrement,
            'gradenumThick': self.gradenumThick,
            'hasBlockChainQualityCert': self.hasBlockChainQualityCert,
            'hasFreight': self.hasFreight,
            'hasFreightSubsidy': self.hasFreightSubsidy,
            'hasQualityCert': self.hasQualityCert,
            'hasQualityInfo': self.hasQualityInfo,
            'hasShop': self.hasShop,
            'hasVideo': self.hasVideo,
            'isAddBid': self.isAddBid,
            'isAfterSettle': self.isAfterSettle,
            'isAttention': self.isAttention,
            'isBailAllowed': self.isBailAllowed,
            'isBargain': self.isBargain,
            'isCompetitiveRes': self.isCompetitiveRes,
            'isDelayAllowed': self.isDelayAllowed,
            'isFixed': self.isFixed,
            'isLoanAllowed': self.isLoanAllowed,
            'isLotteryTime': self.isLotteryTime,
            'isMorgageAllowed': self.isMorgageAllowed,
            'isQuicklyWarehousing': self.isQuicklyWarehousing,
            'isRolled': self.isRolled,
            'isTargeting': self.isTargeting,
            'itemId': self.itemId,
            'itemShape': self.itemShape,
            'latitude': self.latitude,
            'location': self.location,
            'longitude': self.longitude,
            'manufactureCode': self.manufactureCode,
            'manufactureDate': self.manufactureDate,
            'manufactureName': self.manufactureName,
            'maxDeduction': self.maxDeduction,
            'maxPrice': self.maxPrice,
            'midTagPicUrl': self.midTagPicUrl,
            'minPrice': self.minPrice,
            'minPublishTime': self.minPublishTime,
            'modiDate': self.modiDate,
            'modiPerson': self.modiPerson,
            'morgageOrgCode': self.morgageOrgCode,
            'morgageOrgName': self.morgageOrgName,
            'morgageType': self.morgageType,
            'netWeight': self.netWeight,
            'newResource': self.newResource,
            'onBusiness': self.onBusiness,
            'ownerCode': self.ownerCode,
            'ownerName': self.ownerName,
            'packCode': self.packCode,
            'packType': self.packType,
            'paintType': self.paintType,
            'penaltyAmt': self.penaltyAmt,
            'penaltyAmtRate': self.penaltyAmtRate,
            'pieces': self.pieces,
            'prodCat': self.prodCat,
            'productCode': self.productCode,
            'productName': self.productName,
            'productTypeCode': self.productTypeCode,
            'productTypeName': self.productTypeName,
            'promiseTime': self.promiseTime,
            'promotionIds': self.promotionIds,
            'promotionTypes': self.promotionTypes,
            'providerCode': self.providerCode,
            'providerCodeEncode': self.providerCodeEncode,
            'providerName': self.providerName,
            'providerPackCode': self.providerPackCode,
            'providerProductCode': self.providerProductCode,
            'providerProductName': self.providerProductName,
            'providerProductTypeCode': self.providerProductTypeCode,
            'providerProductTypeName': self.providerProductTypeName,
            'providerResCode': self.providerResCode,
            'providerShortName': self.providerShortName,
            'providerShowName': self.providerShowName,
            'publishDate': self.publishDate,
            'publishPrice': self.publishPrice,
            'putinDate': self.putinDate,
            'qualityFlag': self.qualityFlag,
            'qualityGrade': self.qualityGrade,
            'qualityGradeName': self.qualityGradeName,
            'quantity': self.quantity,
            'quickInvoicingFlag': self.quickInvoicingFlag,
            'realEndDate': self.realEndDate,
            'realPictureStatus': self.realPictureStatus,
            'recentBought': self.recentBought,
            'refShopSign': self.refShopSign,
            'resFrom': self.resFrom,
            'resStatus': self.resStatus,
            'resourceId': self.resourceId,
            'resourceType': self.resourceType,
            'rzBankList': self.rzBankList,
            'saleUserName': self.saleUserName,
            'saleUserPhone': self.saleUserPhone,
            'salesMethod': self.salesMethod,
            'salesMode': self.salesMode,
            'sellerLevel': self.sellerLevel,
            'sellerMedal': self.sellerMedal,
            'sellerScore': self.sellerScore,
            'shopShortName': self.shopShortName,
            'shopSign': self.shopSign,
            'smallFrontPicUrl': self.smallFrontPicUrl,
            'spec': self.spec,
            'spec1': self.spec1,
            'spec2': self.spec2,
            'spec3': self.spec3,
            'spec4': self.spec4,
            'spec5': self.spec5,
            'spec6': self.spec6,
            'specComment': self.specComment,
            'specialComments': self.specialComments,
            'startingPrice': self.startingPrice,
            'stdIncrement': self.stdIncrement,
            'stockFlag': self.stockFlag,
            'storeCityCode': self.storeCityCode,
            'storeCityName': self.storeCityName,
            'supervisionRate': self.supervisionRate,
            'surfaceDispose': self.surfaceDispose,
            'surfaceProcess': self.surfaceProcess,
            'targetingCodes': self.targetingCodes,
            'techStandard': self.techStandard,
            'tensionKl': self.tensionKl,
            'tensionQf': self.tensionQf,
            'tensionSc': self.tensionSc,
            'ticketRate': self.ticketRate,
            'userCode': self.userCode,
            'videoInspectionFlag': self.videoInspectionFlag,
            'warehouseCode': self.warehouseCode,
            'warehouseName': self.warehouseName,
            'weekendBusiness': self.weekendBusiness,
            'weight': self.weight,
            'weightMethod': self.weightMethod,
            'whValidatedFlag': self.whValidatedFlag
           }
        if goodsInfoes["shopSign"] == "MIX" and self.refShopSign:
            goodsInfoes["shopSign"] = self.refShopSign
        return goodsInfoes

    def to_small_dic(self):
        goodsInfoes = {
            'balanceWeight': self.balanceWeight,
            'basicPrice': self.basicPrice,
            'businessTimes': self.businessTimes,
            'factoryResCode': self.factoryResCode,
            'location': self.location,
            'manufactureName': self.manufactureName,
            'manufactureDate': self.manufactureDate,
            'resourceId': self.resourceId,
            'packCode': self.packCode,
            'productName': self.productName,
            'productTypeCode': self.productTypeCode,
            'productTypeName': self.productTypeName,
            'publishPrice': self.publishPrice,
            'qualityFlag': self.qualityFlag,
            'qualityGrade': self.qualityGrade,
            'qualityGradeName': self.qualityGradeName,
            'shopSign': self.shopSign,
            'spec': self.spec,
            'specComment': self.specComment,
            'specialComments': self.specialComments,
            'storeCityName': self.storeCityName,
            'techStandard': self.techStandard,
            'ticketRate': self.ticketRate,
            'weight': self.weight,
           }
        if goodsInfoes["shopSign"] == "MIX" and self.refShopSign:
            goodsInfoes["shopSign"] = self.refShopSign
        goodsInfoes["businessTimes"] = "20" + goodsInfoes["businessTimes"]
        return goodsInfoes

    def to_little_dic(self):
        goodsInfoes = {
            'modiDate':self.modiDate,
            'balanceWeight': self.balanceWeight,
            'weight': self.weight,
            'publishDate': self.publishDate,
            'publishPrice': self.publishPrice,
            'basicPrice': self.basicPrice,
            'manufactureName': self.manufactureName,
            'packCode': self.packCode,
            'ticketRate': self.ticketRate,
            'shopSign': self.shopSign,
            'spec': self.spec,
            'specComment': self.specComment,
            'specialComments': self.specialComments,
            'productTypeCode': self.productTypeCode,
            'productTypeName': self.productTypeName,
            'qualityGrade': self.qualityGrade,
            'qualityGradeName': self.qualityGradeName,
            'productName': self.productName,
            'warehouseName': self.warehouseName,
            'spec1': self.spec1,
            'spec2': self.spec2,
            'spec3': self.spec3,
            'spec4': self.spec4,
            'spec5': self.spec5,
            'spec6': self.spec6,
            'storeCityName': self.storeCityName,
            'techStandard': self.techStandard,
           }
        if goodsInfoes["shopSign"] == "MIX" and self.refShopSign:
            goodsInfoes["shopSign"] = self.refShopSign
        return goodsInfoes

    class Meta:
        db_table = 'Ouyeel'
        indexes = [
            models.Index(fields=['basicPrice']),
            models.Index(fields=['publishPrice']),
            models.Index(fields=['providerName']),
            models.Index(fields=['publishDate']),
            models.Index(fields=['manufactureName']),
            models.Index(fields=['shopSign']),
            models.Index(fields=['spec']),
            models.Index(fields=['qualityGrade']),
            models.Index(fields=['qualityGradeName']),
            models.Index(fields=['productCode']),
        ]

